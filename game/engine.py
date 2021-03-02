#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from typing import Type
from datetime import datetime as dte

class Engine:
    def __init__(self, title, version, creator):
        self.title = title
        self.version = version
        self.creator = creator
        self.root_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.start_time = self.StartProcess()
        self.end_time = None
        self.exec_time = None

        ### OS only properties
        self.linux = False
        self.macintosh = False
        self.windows = False

        ### environment
        self.env = os.environ

        self.username = self.GetHostname()

        self.GetOsName()

        print(f"{self.title} - {self.version} (Alpha) (c) {self.creator}")
        print(f"{self.username} has launched process at: {self.start_time}\n\n")

    ### Program-Execution methods
    def StartProcess(self) -> dte:
        self.start_time = dte.now()
        return self.start_time

    def EndProcess(self):
        self.end_time = dte.now()
        self.exec_time = self.end_time-self.start_time
        self.quit()

    def quit(self):
        print(f"\n\n{self.title} - {self.version} finished at: {self.end_time}")
        print(f"Process Execution Time: {self.exec_time}\n\n")
        exit()

    ### OS only methods
    def GetOsName(self):
        if os.name == "posix": ### This is Linux systems
            self.linux = True
        elif os.name == "nt": ### This is Macintosh systems
            self.macintosh = True
        else: ### We fall on the windows systems
            self.windows = True

    def GetUsername(self):
        if self.linux is True or self.windows is True:
            return os.getlogin()

    def GetHostname(self):
        return self.env["HOSTNAME"]


    ### Environment
    def AddToEnvironment(self, variable, value):
        self.env[variable] = value


    ### Engine utilities
    def IsAttribute(self, attribute_name, object):
        properties = self.StoreObjectAttributesDict(object)
        print(properties, "\n\n\n")
        if attribute_name in properties:
            return True
        else:
            return False


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
            
    class ZaFloat():
        def __init__(self, nbr):
            self.attr = float(nbr)

        def __repr__(self) -> float:
            return float(self.attr)