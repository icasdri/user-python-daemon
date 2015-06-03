# Copyright 2014 icasdri
__author__ = 'icasdri'

import dbus
from subprocess import Popen
from sys import argv

path_to_mono = "/usr/bin/mono"
path_to_keepass = "/usr/share/keepass/KeePass.exe"

def _handle_signal(active):
    if active:
        Popen([path_to_mono, path_to_keepass, "--lock-all"])

def entry_point(options=None):
    if options is not None and len(options) == 2:
        global path_to_mono, path_to_keepass
        path_to_mono, path_to_keepass = options
    dbus.SessionBus().add_signal_receiver(_handle_signal, "ActiveChanged", "org.gnome.ScreenSaver")
