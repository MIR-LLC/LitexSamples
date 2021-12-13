#!/usr/bin/env python3

import time

from litex import RemoteClient

wb = RemoteClient()
wb.open()

# # #

wb.regs.gpu_y0.write (200)
wb.regs.gpu_y1.write (240)

for i in range(100):
    for j in range (600):
         wb.regs.gpu_x1.write (j+39)
         wb.regs.gpu_x0.write (j)
         time.sleep(0.001)

wb.close()
