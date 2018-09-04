from enaml.widgets.api import (
    MainWindow, Container, Timer, MenuBar, Menu, Action, PushButton  # Label, Window
    )
from pyqtgraph_widgets import PlotWidget, VideoWidget  # ImageWidgetLeak
from enaml.layout.geometry import Size
from enaml.layout.api import vbox  # hbox, align
# noinspection PyUnresolvedReferences
from enaml.stdlib.message_box import information

from enaml_video_model import Model
import os.path

model = Model(file=os.path.expanduser(r'~\Desktop\cosmos_laundromat.mp4'), device=1)
# https://cloud.blender.org/p/cosmos-laundromat/
