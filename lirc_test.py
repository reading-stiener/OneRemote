

import lirc
from py_irsend import irsend
print(irsend.list_remotes()) 


while True:
    sockid = lirc.init("myprogram")
    print(lirc.nextcode())
    lirc.deinit()