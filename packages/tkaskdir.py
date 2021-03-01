#!/usr/bin/env python


# This is used on Linux and Mac to prompt the user for the projects
# directory.

import sys


# Gtk generally has better support than TKinter on various Linux distributions
def gtk_select_directory(title):
    dialog = Gtk.FileChooserNative(title=title,
                                   action=Gtk.FileChooserAction.SELECT_FOLDER)

    dialog.run()

    return dialog.get_filename()


# Fall back to TKinter if Gtk isn't available
def tk_select_directory(initialdir, title):
    root = Tk()
    root.withdraw()

    return askdirectory(initialdir=initialdir, parent=root, title=title)


try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    def select_directory(title):
        result = gtk_select_directory(title)

        return result if result else ''

except:
# Python3 and Python2-style imports.
    try:
        from tkinter import Tk
        from tkinter.filedialog import askdirectory
    except ImportError:
        from Tkinter import Tk
        from tkFileDialog import askdirectory

    def select_directory(title):
        return tk_select_directory(title, sys.argv[1])

if __name__ == '__main__':
    directory = select_directory(f'Select {game.title} Directory')

    sys.stdout.write(directory)
