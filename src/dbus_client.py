'''
Created on Oct 25, 2012

@author: nemo
'''

import dbus


dbus = dbus.SessionBus()
my_dbus_proxy = dbus.get_object('home.nemo.my_dbus', '/home/nemo/my_dbus')

for i in range(10):
    my_dbus_proxy.print_num(i)
