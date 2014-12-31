# Copyright 2014 icasdri
__author__ = 'icasdri'

import argparse
import os.path
import configparser
import sys
import importlib

DESCRIPTION = "..."
VERSION = 0.1


def _parse_args(options=None):
    a_parser = argparse.ArgumentParser(prog="user-python-daemon",
                                       description=DESCRIPTION)
    a_parser.add_argument("--config-file", type=str,
                          help="configuration file to use")
    a_parser.add_argument("--version", action='version', version="%(prog)s v{}".format(VERSION))
    if options is None:
        args = a_parser.parse_args()
    else:
        args = a_parser.parse_args(options)

    module_names = []
    module_paths = []

    if args.config_file is None:
        args.config_file = os.path.expanduser("~") + "/.config/user_python_daemon.conf"
    if os.path.isfile(args.config_file):
        c_parser = configparser.ConfigParser()
        for section in c_parser.sections():
            if "module" in section:
                module_names.append(section["module"])
                if "path" in section:
                    module_paths.append(section["path"])

    return module_names, module_paths

def main(options=None):
    module_names, module_paths = _parse_args(options)

    from dbus.mainloop.glib import DBusGMainLoop
    from gi.repository.GObject import MainLoop

    DBusGMainLoop(set_as_default=True)

    for path in module_paths:
        sys.path.append(path)

    for name in module_names:
        importlib.import_module(name).entry_point()

    del module_names, module_paths

    MainLoop().run()

