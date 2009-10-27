#!/usr/bin/env python

import indicate 
import gobject 
import gtk 
from time import time 
import os

curdir = os.getcwd()
desktop_file = os.path.join(curdir, "weechat.desktop")
#desktop_file = '/usr/share/applications/epiphany.desktop'

def display(indicator):

    print "Ah, my indicator has been displayed"
    indicator.hide()

def server_display(server):

    print "Ah, my server has been displayed"

if __name__ == "__main__":

    # Setup the server
    server = indicate.indicate_server_ref_default()
    server.set_type("message.im")
    server.set_desktop_file(desktop_file)
    server.connect("server-display", server_display)
    server.show()

    # Setup the message
    try:
      # Ubuntu 9.10 and above
      indicator = indicate.Indicator()
    except:
      # Ubuntu 9.04
      indicator = indicate.IndicatorMessage()

    indicator.set_property("subtype", "im")
    indicator.set_property("sender", "Test message")
    indicator.set_property("body", "Test message body")
    indicator.set_property_time("time", time())
    indicator.show()
    indicator.connect("user-display", display)
    indicator.set_property('draw-attention', 'true');

    # Loop
    gtk.main()
