#!/usr/bin/env python3
# Copyright 2014 icasdri
__author__ = 'icasdri'

import dbus
import dbus.service
from gi.repository import Notify

MY_BUS_NAME = "org.icasdri.thunderbirdnotifications"
MY_INTERFACE = MY_BUS_NAME
MY_PATH = "/org/icasdri/thunderbirdnotifications"


class ThunderbirdNotifications(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName(MY_BUS_NAME, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, MY_PATH)

        Notify.init("Thunderbird Notifications")

    @dbus.service.method(dbus_interface=MY_INTERFACE)
    def ProxyNotify(self, summary, body, icon="mail-mark-unread"):
        notification = Notify.Notification.new(summary, body, icon)
        notification.set_category("email.arrived")
        notification.show()

def entry_point(options=None):
    ThunderbirdNotifications()


# This module is designed to mimick 'notify-send' if run directly -- contacting an
# already running daemonized version of this module (through user-python-daemon) and
# proxying the notification.
def main():
    import argparse
    a_parser = argparse.ArgumentParser("Thunderbird Notifications Proxy (part of user-python-daemon)",
                                       "Use like notify-send.")
    a_parser.add_argument("summary", type=str)
    a_parser.add_argument("body", type=str)
    a_parser.add_argument("-i", "--icon", type=str, default="mail-mark-unread")
    args, unknown = a_parser.parse_known_args()
    if MY_BUS_NAME in dbus.SessionBus().list_names():
        dbus.Interface(dbus.SessionBus().get_object(MY_BUS_NAME, MY_PATH), MY_INTERFACE)\
            .ProxyNotify(args.summary, args.body, args.icon)
        print("Notification sent to proxy daemon.")
    else:
        print("Daemonized version of module (accessible via entry_point() function, "
              "see user-python-daemon) is not running! Exitting.")


if __name__ == "__main__":
    main()
