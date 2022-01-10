#!/usr/bin/env python3

from litex import RemoteClient

wb = RemoteClient()
wb.open()


# # #
# Fill Memory
for i in range(512):
    wb.write (wb.mems.wbram.base+i*4,i)

# Check Memory Content
for i in range(512):
    if (wb.read (wb.mems.wbram.base+i*4) != i):
         print ("Errror at  ",i,":",wb.read (wb.mems.wbram.base+i*4));

print ("Test Finished");
wb.close()
