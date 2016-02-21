#!/usr/bin/env python

import gi
# May or may not be needed :
gi.require_version('WebKit', '3.0')
gi.require_version('Gtk', '3.0')

# "WebKit" NOT "webkit" :
# "Gtk" NOT "gtk" :
from gi.repository import Gtk,Gdk,WebKit




win= Gtk.Window()


box1 = Gtk.VBox()
win.add(box1)

box2 = Gtk.HBox()
box1.pack_start(box2, False, False, False)

addressbar = Gtk.Entry()
box2.pack_start(addressbar, False, False, False)

win.show_all()
Gtk.main()
