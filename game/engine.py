#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from typing import Type

class Engine:
    def __init__(self, title, version, creator):
        self.title = title
        self.version = version
        self.creator = creator
        self.root_path = os.path.dirname(os.path.realpath(sys.argv[0]))

        ### OS only properties
        self.linux = False
        self.macintosh = False
        self.windows = False

        ### environment
        self.env = os.environ

        self.username = self.GetHostname()

        self.GetOsName()

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
            r += f"{key}: {value}\n"
        return r

    def ListToStr(self, l): ### l = list
        pass

    ###  Engine-defined Classes
    class ZaList(object):
        def __init__(self, liste):
            self.attr = list(liste)

        def __class__(self):
            pass
        
        def __call__(self):
            return self.attr

    class ZaDict(object):
        def __init__(self, key, value):
            self.attr = dict((key, value))