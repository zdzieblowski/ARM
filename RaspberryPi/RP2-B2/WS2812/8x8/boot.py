from libs import Neopixel
import utime
import math
import uasyncio

matrix_size = 64
matrix_w = 8
matrix_h = matrix_size/matrix_w

matrix = Neopixel(matrix_size, 0, 15, "GRB", matrix_w, 0)
matrix.brightness(2)

matrix.mClear()

# CORNER TEST

utime.sleep(1)

cornerTest = [(255,255,255),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(255,255,255),
              (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
              (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
              (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
              (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
              (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
              (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
              (255,255,255),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(255,255,255)]

matrix.mDrawData(cornerTest)

utime.sleep(5)

matrix.mClear()

utime.sleep(.5)

# COLOR TEST

i = 0

loop = uasyncio.get_event_loop()

colors = []
for p in range(0, matrix_size):
    colors.append(matrix.colorHSV(i*1024+p*1024,255,255))

async def colorTest():
     
    matrix.mDrawData(colors)

    temp = colors[0]
    colors.pop(0)
    colors.append(temp)

    loop.create_task(colorTest())

async def runColorTest():
    loop.create_task(colorTest())
    await uasyncio.sleep(5)
    loop.stop()
    matrix.mClear()

uasyncio.run(runColorTest())
