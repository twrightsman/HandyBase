# application.py
#
# Copyright 2020 Travis Wrightsman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import List

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")

from gi.repository import Gtk, Gio, Gdk, Handy

from .window import HandyBaseWindow


class HandyBase(Gtk.Application):
    def __init__(self):
        super().__init__(
            application_id="io.github.twrightsman.HandyBase",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
        )

        # load application stylesheet
        default_css = Gtk.CssProvider()
        default_css.load_from_resource("/io/github/twrightsman/HandyBase/style/handybase.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            default_css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

    def do_startup(self):
        Gtk.Application.do_startup(self)
        Handy.init()

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = HandyBaseWindow(application=self)

        win.show_all()
        win.present()
