# Copyright 2014 icasdri
__author__ = 'icasdri'

import argparse
import os.path
import configparser
import sys
import importlib
import logging

log = logging.getLogger(__name__)

DESCRIPTION = "..."
VERSION = 0.1

NO_OPTIONS = []


def _parse_args(options=None):
    a_parser = argparse.ArgumentParser(prog="user-python-daemon",
                                       description=DESCRIPTION)
    a_parser.add_argument("--config-file", type=str,
                          help="configuration file to use")
    a_parser.add_argument("--version", action='version', version="%(prog)s v{}".format(VERSION))
    a_parser.add_argument("--debug", action='store_true')

    if options is None:
        args = a_parser.parse_args()
    else:
        args = a_parser.parse_args(options)

    if args.debug:
        log.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        log.addHandler(handler)

    modules = []
    module_paths = []

    if args.config_file is None:
        args.config_file = os.path.expanduser("~") + "/.config/user_python_daemon.conf"
    if os.path.isfile(args.config_file):
        log.info("Using config file {}".format(args.config_file))
        c_parser = configparser.ConfigParser()
        c_parser.read(args.config_file)
        for name in c_parser.sections():
            section = c_parser[name]
            if "path" in section:
                module_paths.append(os.path.expanduser(section["path"]))
            if "options" in section:
                module = (name, section["options"].split())
            else:
                module = (name, NO_OPTIONS)
            modules.append(module)

    return modules, module_paths

def main(options=None):
    modules, module_paths = _parse_args(options)

    from dbus.mainloop.glib import DBusGMainLoop
    from gi.repository.GObject import MainLoop

    DBusGMainLoop(set_as_default=True)

    for path in module_paths:
        log.info("Appending path {}".format(module_paths))
        sys.path.append(path)

    for module_name, module_options in modules:
        log.info("Invoking entry_point() on module {} with options {}".format(module_name, module_options))
        importlib.import_module(module_name).entry_point(module_options)

    log.info("Removing unnecessary resources and entering MainLoop")
    del modules, module_paths, module_name, module_options, path

    MainLoop().run()

if __name__ == "__main__":
    main()
