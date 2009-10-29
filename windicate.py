# Author: Leon Bogaert <leon AT tim-online DOT nl>
# This Plugin Calls the libindicate bindings via python when somebody says your
# nickname, sends you a query, etc.
# To make it work, you may need to download: python-indicate
# Requires Weechat 0.3.0
# Released under GNU GPL v2
#
# 2009-10-29, Leon <leon@tim-online.nl>:
#     version 0.0.1 Intial release
# 
# @TODO: find out how to jump to buffer/line
# @TODO: decide what to do if a user clicks an indicator an then start typing:
#        * leave indicators alone
#        * remove indicators in the "neighbourhood"


import weechat, pynotify, string

weechat.register("windicate", "Leon Bogaert", "0.0.1", "GPL", 
                 "fills the indicate applet", "", "")

# script options
settings = {
    "show_hilights"             : "on",
    "show_priv_msg"             : "on",
    "time_between_msg"          :    5,
}

# Init everything
for option, default_value in settings.items():
    if weechat.config_get_plugin(option) == "":
        weechat.config_set_plugin(option, default_value)

# Hook privmsg/hilights
weechat.hook_print("", "", "", 1, "       nofify_show_hi",   "")
weechat.hook_signal("weechat_highlight", "nofify_show_hi",   "")
weechat.hook_signal("weechat_pv",        "nofify_show_priv", "")
