from enaml.widgets.api import (
    MainWindow, Container, Timer, MenuBar, Menu, Action, PushButton  # Label, Window
    )
from pyqtgraph_widgets import PlotWidget, VideoWidget
from enaml.layout.geometry import Size
from enaml.layout.api import vbox  # hbox, align
from enaml.application import deferred_call
# noinspection PyUnresolvedReferences
from enaml.stdlib.message_box import information

from enaml_video_model import Model
import os.path
import shortcutter

sc = shortcutter.ShortCutter()
model = Model(file=os.path.join(sc.desktop_folder, 'cosmos_laundromat.mp4'), device=0)
# https://cloud.blender.org/p/cosmos-laundromat/
