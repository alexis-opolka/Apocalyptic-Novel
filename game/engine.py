#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from libs.typeshed import *
import PyQt5

#///////////////////////////////////////////////
#   Keep this part for further check
#   but nearly sure won't be needed for long
#///////////////////////////////////////////////


#try:
#    import PyQt5.QtWebKitWidgets as PyQtWebWidgets ### Support for Linux
#    from PyQtWebWidgets import QWebView
#except:
#    from PyQt5.QtWebEngineWidgets import *


#///////////////////////////////////////////////

from PyQt5.QtGui import (
    QIcon,
    QPixmap,
    QKeySequence,
)
from PyQt5.QtWebEngineWidgets import (
    QWebEngineView,
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QTabWidget,
    QLineEdit,
    QGridLayout,
    QFrame,
    QShortcut,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtCore import (
    Qt,
    QUrl,
)

import os
import sys
import platform
import urllib
from typing import Type
from datetime import datetime as dte

class Engine:
    def __init__(self, title, version, creator):

        ### Program-wide properties
        self.title = title
        self.version = version
        self.creator = creator
        self.root_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.start_time = None
        self.end_time = None
        self.exec_time = None
        self.example_host = "http://www.gitlab.com" ### An host used as an example to check wifi connectivity

        ### OS-related properties
        self.supported_os = ["Linux", "Windows"]
        self.linux = False
        self.windows = False
        self.platform = ""

        ### environment
        self.env = os.environ
        self.GetOsName()
        if self.linux is True:
            self.username = self.GetHostname()
        else:
            self.username = self.GetUsername()
        self.wifi = {} ### `nom du wifi`, `True` si connecté sinon `False`

        self.Qt_app = QApplication(sys.argv)
        self.window = VisualEngine(self, self.title)
        self.browser = WebBrowser(self, str(self.title + " browser"))
        self.window.windows.append(self.browser)

        self.StartProcess()

        print(f"{self.title} - {self.version} (Alpha) (c) {self.creator}")
        print(f"{self.username} has launched process at: {self.start_time}\n\n")


    ### Program-Execution methods
    def StartProcess(self):
        self.start_time = dte.now()

    def EndProcess(self):
        self.end_time = dte.now()
        self.exec_time = self.end_time-self.start_time
        self.quit()

    def quit(self):
        print(f"\n\n{self.title} - {self.version} finished at: {self.end_time}")
        print(f"Process Execution Time: {self.exec_time}")
        print(f"Ran on {self.platform if self.platform != '' else None}\n\n")
        exit()

    ### OS-related methods
    def GetOsName(self):
        system = platform.system()

        if system in self.supported_os:
            self.platform = system
            if system == "Linux":
                self.SetVariable("linux", True)
            else:
                self.SetVariable("windows", True)
        else:
            raise Exception("SupportError: Sorry, you launched the game with a system which we don't support.")

    def GetUsername(self):
        return os.getlogin()

    def GetHostname(self):
        return self.env["HOSTNAME"]


    ### Environment
    def AddToEnvironment(self, variable, value):
        self.env[variable] = value


    ### Engine utilities
    #### Methods used in conditions
    def IsAttribute(self, object, attribute_name):
        properties = self.StoreObjectAttributesDict(object)
        if attribute_name in properties:
            return True
        else:
            return False

    def IsWifiOn(self):
        try:
            urllib.request.urlopen(self.example_host) #Python 3.x
            return True
        except:
            return False

    #### Methods for actions
    def StartQtProcess(self, verify=False, maximized=False):
        if verify is True:
            execute = input("Do you want to launch the QT window [Y/N]: ")
            if execute.lower() == "y":
                if maximized is False:
                    self.window.exec()
                else:
                    self.window.execMaximized()
                self.Qt_app.exec_()
            else:
                return
        else:
            if maximized is False:
                self.window.exec()
            else:
                self.window.execMaximized()
            self.Qt_app.exec_()

    def OpenBrowser(self):
        self.browser.show()

    ### Variables-access related methods
    def SetVariable(self, variable, value):
        if self.IsAttribute(self, variable):
            variable = value
        else:
            exec(f"""global {variable}\n{variable} = {value}""")

    def ToggleVariable(self, variable, kind_one=None, kind_two=None):
        if kind_one is None and kind_two is None:
            if type(variable) in [bool, NoneType]:
                if variable is False:
                    variable = True
                else:
                    variable = False
        else:
            if variable == kind_one:
                variable = kind_two
            else:
                variable = kind_one

    ### Debug utilities
    #### Object-wide related methods
    def StoreObjectAttributesDict(self, object):
        attr = {p:getattr(object, p) for p in dir(object)}
        return attr

    #### Str-related methods
    def DictToStr(self, dict):
        r = ""
        for key, value in dict.items():
            r += f"- {key}: {value}\n"
        return r

    def ListToStr(self, list): ### l = list
        r = ""
        for elem in list:
            r += f"- {elem}\n"
        return r

###  Engine-defined Classes
class ZaList(object):
    def __init__(self, liste):
        self.attr = list(liste)

    def __class__(self):
        pass

    def __call__(self):
        return self.attr

    def __repr__(self) -> str:
        return str(self.attr)

class ZaDict(object):
    def __init__(self, key, value):
        self.attr = dict(key=value)

    def __class__(self):
        pass

    def __repr__(self) -> str:
        return str(self.attr)

class ZaStr(object):
    def __init__(self, string):
        self.attr = str(string)

    def __repr__(self) -> str:
        return str(self.attr)

class ZaInt(object):
    def __init__(self, integer):
        self.attr = int(integer)

    def __repr__(self) -> int:
        return int(self.attr)

class ZaFloat(object):
    def __init__(self, nbr):
        self.attr = float(nbr)

    def __repr__(self) -> float:
        return float(self.attr)

class VisualEngine(QMainWindow):
    def __init__(self, root, window_title):
        super().__init__()
        self.root = root
        self.windows = []
        self.window_title = window_title
        self.button = QPushButton("Push to change Widgets")
        self.button.clicked.connect(self.show_new_window)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setCentralWidget(self.button)

        QShortcut(QKeySequence("Ctrl+Q"), self, self.quit)

    def show_new_window(self, checked):
        #self.hide()
        self.windows.append(self.root.browser)
        self.setWindowTitle(self.root.browser.window_title)
        self.setCentralWidget(self.root.browser)
        #self.root.browser.execMaximized()

    def exec(self):
        self.root.Qt_app.setApplicationName(self.window_title)
        self.setWindowTitle(self.window_title)
        self.windows.append(self)
        self.show()

    def execMaximized(self):
        self.root.Qt_app.setApplicationName(self.window_title)
        self.setWindowTitle(self.window_title)
        self.windows.append(self)
        self.showMaximized()

    def quit(self):
        self.close()

class WebBrowser(QMainWindow):
    def __init__(self, root, window_title):
        super().__init__()
        self.root = root
        self.window_title = window_title

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel("Here is the WebBrowser() window")
        layout.addWidget(self.label)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeTab)
        self.tab1 = QWidget()
        self.tabWebView = []
        self.lNameLine = []
        self.tabs.addTab(self.tab1,"New Tab")
        self.tab1UI(self.tab1)
        self.setCentralWidget(self.tabs)

        QShortcut(QKeySequence("Ctrl+T"), self, self.addTab)
        QShortcut(QKeySequence("Ctrl+W"), self, self.closeTab)

    def exec(self):
        self.root.Qt_app.setApplicationName(self.window_title)
        self.setWindowTitle(self.window_title)
        self.show()

    def execMaximized(self):
        self.root.Qt_app.setApplicationName(self.window_title)
        self.setWindowTitle(self.window_title)
        self.showMaximized()

    def addTab(self):
      tab = QWidget()
      self.tabs.addTab(tab,"New Tab")
      self.tab1UI(tab)

      index = self.tabs.currentIndex()
      self.tabs.setCurrentIndex( index + 1 )
      self.tabWebView[self.tabs.currentIndex()].load( QUrl('https://duckduckgo.com'))

    def goBack(self):
      index = self.tabs.currentIndex()
      self.tabWebView[index].back()

    def goNext(self):
      index = self.tabs.currentIndex()
      self.tabWebView[index].forward()

    def goRefresh(self):
      index = self.tabs.currentIndex()
      self.tabWebView[index].reload()

    def changePage(self):
        index = self.tabs.currentIndex()
        pageTitle = self.sender().title()[:15]
        self.tabs.setTabText(index, pageTitle)
        self.lNameLine[self.tabs.currentIndex()].setText(self.sender().url().url())

    def load_started(self):
       return

    def tab1UI(self,tabName):
        webView = QWebEngineView()

        backButton = QPushButton("<-")
        #backIcon = QIcon()
        #backIcon.addPixmap(QPixmap("back.svg"))
        #backButton.setIcon(backIcon)
        backButton.setFlat(True)

        nextButton = QPushButton("->")
        #nextIcon = QIcon()
        #nextIcon.addPixmap(QPixmap("next.svg"))
        #nextButton.setIcon(nextIcon)
        nextButton.setFlat(True)

        refreshButton = QPushButton("O")
        #refreshIcon = QIcon()
        #refreshIcon.addPixmap(QPixmap("refresh.svg"))
        #refreshButton.setIcon(refreshIcon)
        refreshButton.setFlat(True)

        backButton.clicked.connect(self.goBack)
        nextButton.clicked.connect(self.goNext)
        refreshButton.clicked.connect(self.goRefresh)

        self.newTabButton = QPushButton("+")
        self.destroyTabButton = QPushButton("-")
        self.tabWidget = QTabWidget()

        nameLine = QLineEdit()
        nameLine.returnPressed.connect(self.requestUri)

        tabGrid = QGridLayout()

        tabGrid.setContentsMargins(0,0,0,0)

        navigationFrame = QWidget()
        navigationFrame.setMaximumHeight(32)

        navigationGrid = QGridLayout(navigationFrame)
        navigationGrid.setSpacing(0)
        navigationGrid.setContentsMargins(0,0,0,0)
        navigationGrid.addWidget(backButton,0,1)
        navigationGrid.addWidget(nextButton,0,2)
        navigationGrid.addWidget(refreshButton,0,3)
        navigationGrid.addWidget(nameLine,0,4)

        tabGrid.addWidget(navigationFrame)

        html_head = ""
        webView.setHtml(html_head)
        webView.setStyleSheet("background-color:#1a1a1a;")

        #webView.loadProgress.connect(self.loading)
        webView.loadFinished.connect(self.changePage)

        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)

        gridLayout = QGridLayout(frame)
        #gridLayout.setObjectName(QStringLiteral("gridLayout"));
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.addWidget(webView, 0, 0, 1, 1)
        frame.setLayout(gridLayout)

        self.tabWebView.append(webView)
        self.tabWidget.setCurrentWidget(webView)
        self.lNameLine.append(nameLine)
        tabGrid.addWidget(frame)
        tabName.setLayout(tabGrid)

    def tab2UI(self):
        vbox = QVBoxLayout()
        tbl1 = QTableWidget()
        tbl1.setRowCount(5)
        tbl1.setColumnCount(5)
        vbox.addWidget(tbl1)
        tbl1.setItem(0, 0, QTableWidgetItem("1")) # row, col
        self.tab2.setLayout(vbox)

    def requestUri(self):
       if self.tabs.currentIndex() != -1:

           urlText = self.lNameLine[self.tabs.currentIndex()].text()

           ##########################
           # no protocol?
           if 'http' not in urlText:
               self.lNameLine[self.tabs.currentIndex()].setText( 'https://' + urlText)

           url = QUrl(self.lNameLine[self.tabs.currentIndex()].text())

           print(self.tabs.currentIndex())
           if url.isValid():
               self.tabWebView[self.tabs.currentIndex()].load(url)
           else:
               print("Url not valid")
       else:
           print("No tabs open, open one first.")

    def closeTab(self, tabId=None):
        if tabId == None:
            tabId = self.tabs.currentIndex()
        #if self.tabs.currentIndex() == (0):
        #    self.root.window.windows.pop(self.root.window.windows.index(self.root.browser))
        #    self.setWindowTitle(self.root.window.window_title)
        #    self.setCentralWidget(self.root.window)
        del self.lNameLine[tabId]
        del self.tabWebView[tabId]
        self.tabs.removeTab(tabId)

    def load_page(self, widget):
        so_add = self.wow_address_bar.get_text()
        if so_add.startswith('http://') or so_add.startswith('https://'):
            self.such_webview.open(so_add)
        else:
            so_add = 'http://' + so_add
            self.wow_address_bar.set_text(so_add)
            self.such_webview.open(so_add)

    def change_title(self, widget, frame, title):
        self.much_window.set_title('Wow So ' + title)

    def change_url(self, widget, frame):
        uri = frame.get_uri()
        self.wow_address_bar.set_text(uri)

    def go_back(self, widget):
        self.such_webview.go_back()

    def go_forward(self, widget):
        self.such_webview.go_forward()

    def refresh_page(self, widget):
        self.such_webview.reload()
