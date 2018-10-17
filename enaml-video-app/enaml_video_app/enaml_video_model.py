from atom.api import Atom, Typed, Unicode, Int, Bool, Signal
from enaml.core.declarative import d_
from enaml.application import deferred_call
from time import sleep
from collections import deque
from threading import Thread

from numpy import ndarray
import numpy as np
from typing import Tuple

import os.path as p
from .lib import cv


CAP_PERIOD = 0.020  # capture period in seconds


def edit_frame(frame: ndarray, y: int) -> Tuple[ndarray, ndarray]:
    """
    Parameters
    ----------
    frame : (is row-major)
    y

    Returns
    -------
    (frame, cut)
    """
    np.random.uniform(-1, 1, size=20000000)  # 20000000@6cores
    cut = cv.cvtColor(frame[[y], :], cv.COLOR_BGR2GRAY)[0, :]
    # Convert OpenCV colors to PyQtGraph colors
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    return frame, cut


class Model(Atom):
    """
    Read: Просто читаю кадры и кладу в очередь через период (в отдельном потоке).
        Период либо берется из свойств файла, либо константа (10 мс) - если мы не знаем свойств источника.
    Edit: По таймеру, через (другой) период беру последний кадр из очереди и обрабатываю его (в основном потоке).
    Out: После обработки сразу же вывожу (сразу же в том же куске кода).

    Constructor parameters
    ----------------------
    file : Unicode = ''
        Video file path
    device : Int = 0
        OpenCV device ID used only if the file doesn't exist
    """
    file = Unicode('')
    device = Int(0)
    captured_frames = Typed(deque)
    edited_frames = Typed(deque)
    y = d_(Int(0))
    capturing = d_(Bool(True))
    update = Signal()

    def start_capturing(self):
        """
        Starts workers threads.
        """
        self.captured_frames = deque()
        self.edited_frames = deque()
        if p.isfile(self.file):
            capture = cv.VideoCapture(self.file)
            period = 1 / capture.get(5)
        else:
            capture = cv.VideoCapture(self.device)
            period = CAP_PERIOD
        thread_capturer = Thread(target=worker_capturer, args=(capture, period, self))
        thread_editor = Thread(target=worker_editor, args=(period / 2, self))
        thread_capturer.daemon = True
        thread_editor.daemon = True
        thread_capturer.start()
        thread_editor.start()

    def frame_and_cut(self) -> Tuple[ndarray, ndarray] or None:
        """
        Pops (frame, cut) from a deque if there are more than one tuple inside.

        Returns
        -------
        (frame, cut) or None
        """
        if len(self.edited_frames) > 1:
            frame, cut = self.edited_frames.pop()
            return frame, cut
        else:
            return None


def worker_capturer(capture, period: float, model: Model):
    """
    Worker function for another thread that captures frames
    and puts them to deque with constant period given.

    Parameters
    ----------
    capture : cv2.VideoCapture()
    period : (in seconds)
    model
    """
    while model.capturing:
        ret, frame = capture.read()
        if frame is not None:
            model.captured_frames.appendleft(frame)
            sleep(period)


def worker_editor(period: float, model: Model):
    """
    Worker function for another thread that edits frames and puts them
    to deque. Edits the latest frame and takes a cut along X axis from it
    (fixed Y coordinate).

    Parameters
    ----------
    period : (in seconds)
    model
    """
    while model.capturing:
        frame = None
        while len(model.captured_frames) > 1:
            frame = model.captured_frames.pop()
        if not (frame is None):
            frame, cut = edit_frame(frame, model.y)
            model.edited_frames.appendleft((frame, cut))
            deferred_call(model.update)
        else:
            sleep(period)
