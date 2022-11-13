from future.types.newint import long
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import maya.cmds

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)

class MayaWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MayaWidget,self).__init__(*args, **kwargs)

        self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Window)

        self.setWindowTitle('Revolve curve around X')
        self.setGeometry(50,50,250,150)

        self.revolve_button = QPushButton('Revolve',self)
        self.curve_name = QTextEdit('Curve Name',self)

        self.revolve_button.clicked.connect(self.revolve_onClicked)

    def revolve_onClicked(self):
        curveName = self.curve_name.toPlainText()
        maya.cmds.revolve(curveName, ax=(1, 0, 0), p = (0, 0, 0))