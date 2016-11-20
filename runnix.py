"""
runnix
------
A Linux (actually it should work on any OS) Win+R emulator.
Have fun messing with scammers!

by David Teresi (aka __init__), June 2016.

runnix.py is basically the main Python code for this. I don't think
I'll need any other files as this is such a simple program :P
"""

# Import modules
from PyQt5 import QtCore, QtWidgets, QtGui, uic
import sys
import os

# QApplication instance
app = QtWidgets.QApplication(sys.argv)

# Directory where all the things are
things = os.path.dirname(os.path.abspath(__file__))
l = lambda f: os.path.join(things, f)

# Form classes for the UI files.
# Each one is for a different window
eventvwr   = uic.loadUi(l('eventvwr.ui'))    #  eventvwr window (displays "no errors found")
msconfig   = uic.loadUi(l('msconfig.ui'))    #  msconfig window (displays "all services running")
virus      = uic.loadUi(l('virus.ui'))       #  Virus protection window. Should display when the scammer enters
                                             # anything about viruses (e.g. "virus protection", "virus", "windows defender")
                                             # Displays "no viruses found"
syskey     = uic.loadUi(l('syskey.ui'))      #  "Syskey" window. This one tells you that a scammer has been detected
junkfiles  = uic.loadUi(l('junkfiles.ui'))   #  Displays "no junk files found." Can be used with prefetch or temp
regedit    = uic.loadUi(l('regedit.ui'))     #  Haven't seen a scammer use regedit yet but it's good to be prepared
msinfo32   = uic.loadUi(l('msinfo32.ui'))    #  MSInfo32 clone, looks just like the real thing


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = uic.loadUi(l('mainwindow.ui'), self)
        self.ui.show()

        self.ui.runIcon.pixmap = l("run_37198.jpg")

        self.okButton.clicked.connect(self.run)
        self.commandBox.lineEdit().returnPressed.connect(self.run)

        self.commandBox.setFocus()

    def run(self):
        print "running run()"
        self.ui.hide()
        contents = self.commandBox.currentText()
        form_class = parse_string(contents)
        show_window(form_class)


class CmdLine(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = uic.loadUi(l('cmd.ui'), self)
        self.ui.show()

        self.plainTextEdit.appendPlainText("Microsoft Windows (Version 10.0.10240)")
        self.plainTextEdit.appendPlainText("(c) 2015 Microsoft Corporation. All rights reserved. \n")

        self.plainTextEdit.appendPlainText("C:\\> ")

        self.plainTextEdit.installEventFilter(self)

        self.editable = True
        self.keys = []
        self.lolnope = []

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress:
            print event.text(),
            if self.editable:
                if (event.key() == QtCore.Qt.Key_Return or
                     event.key() == QtCore.Qt.Key_Enter):
                    self.parse()
                    # bypass default handling
                    return True
                else:
                    self.keys += event.text()
            else:
                self.lolnope += event.text()
                return True
        return super(CmdLine, self).eventFilter(widget, event)

    def parse(self):
        self.editable = False
        s = ''.join(self.keys)
        if s in ('cd..', 'cd ..'):
            self.plainTextEdit.appendPlainText("\n")
        elif s in ('tree', 'dir /s'):
            self.tree()
        elif s == 'netstat':
            self.plainTextEdit.appendPlainText("\nAll incoming and outgoing connections are clean.\nNo foreign addresses detected.\n")
        else:
            self.plainTextEdit.appendPlainText("\n%s is not recognized as an internal or external command,\noperable program or batch file.\n"%s)
        self.keys = []
        self.editable = True
        self.plainTextEdit.insertPlainText("\nC:\\> ")

    def tree(self):
        with open(l('tree.txt'), 'r') as tree_file:
                for line in tree_file:
                    self.plainTextEdit.insertPlainText(line)
                    self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
                    QtWidgets.QApplication.processEvents()
        self.plainTextEdit.appendPlainText("\n\n\n\nNo viruses, malware, trojans or spyware found. Your computer is clean.\n")

    def __del__(self):
        with open(l('lolnope.txt'), 'w') as f:
            f.write(''.join(self.lolnope))


## str -> form class (too lazy to get actual subclass name)

def parse_string(s):
    "Parse string and get form class to load."
    print "parse_string: String arg is %s"%s
    if s in ("eventvwr", "event viewer", "event", "viewer"):
        return eventvwr
    elif s in ("virus", "protection", "virus protection", "windows defender", "defender", "security"):
        return virus
    elif s == "syskey":
        return syskey
    elif s == "msconfig":
        return msconfig
    elif s == "cmd":
        return CmdLine()
    elif "prefetch" in s or "temp" in s:
        return junkfiles
    elif s in ("regedit", "registry"):
        return regedit
    elif s == "msinfo32":
        return msinfo32
    else:
        sys.exit(0)


def test_parse_string():  # Py.test tests
    assert parse_string("eventvwr") == eventvwr
    assert parse_string("event viewer") == eventvwr
    assert parse_string("virus") == virus
    assert parse_string("protection") == virus
    assert parse_string("virus protection") == virus
    assert parse_string("windows defender") == virus
    assert parse_string("defender") == virus
    assert parse_string("syskey") == syskey
    assert parse_string("msconfig") == msconfig


def show_window(form_class):
    "Show window of given form class"
    if not isinstance(form_class, CmdLine):
        try:
            form_class.exec_()
        except AttributeError:
            form_class.show()

window = MainWindow()
app.exec_()
