#!/usr/bin/env python3

import time

from litex import RemoteClient

wb = RemoteClient()
wb.open()

# # #

for i in range(1000):
    print (wb.regs.gpu_frame.read())

wb.close()
