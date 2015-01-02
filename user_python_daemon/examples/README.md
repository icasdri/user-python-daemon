## Examples
Modules in this are small but useful and functional examples of how user-python-daemon can be used to improve desktop functionality. Please feel free to use these modules in a running user-python-daemon -- simply add the corresponding module name to your `user_python_daemon.conf`.

For larger and more involved examples, see [mpris2controller](https://github.com/icasdri/mpris2controller) and [pybatterymonitor](https://github.com/icasdri/pybatterymonitor), which both can be run as part of user-python-daemon.

### GNOME KeePass Autolock

	gnome_keepass_autolock.py

This module is meant to autolock [KeePass](http://keepass.info) workspaces with the [GNOME](http://www.gnome.org/gnome-3/) Screen Saver. In other words, provide KeePass's internal "Lock workspace when locking computer" functionality that is not available in GNU/Linux systems.

To use this module add the following to your user-python-daemon configuration (located at `~/.config/user_python_daemon.conf` by default).

	[user_python_daemon.examples.gnome_keepass_autolock]

### Thunderbird Notifications

	thunderbird_notifications.py

This module is meant to improve the notifications provided by the [Gnome Integration](https://addons.mozilla.org/en-US/thunderbird/addon/gnome-integration/) Plugin for [Thunderbird](https://www.mozilla.org/en-US/thunderbird/) by firing notifications with a consistent Bus Name. This allows for freedesktop notification-compliant desktops with "notification drawers" to properly display Thunderbird notifications as originating from a single application.

To use this module add the following to your user-python-daemon configuration (located at `~/.config/user_python_daemon.conf` by default).

	[user_python_daemon.examples.thunderbird_notifications]

Additionally, in the preferences dialog of the Gnome Integration plugin, use the path to `thunderbird_notifications.py` as the "Command (path to notify-send binary)".