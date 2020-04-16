# window.py
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

from pathlib import Path
from typing import Optional

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")

from gi.repository import Gtk, Handy

@Gtk.Template(resource_path="/io/github/twrightsman/HandyBase/ui/window.ui")
class HandyBaseWindow(Handy.ApplicationWindow):
    __gtype_name__ = "HandyBaseWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
