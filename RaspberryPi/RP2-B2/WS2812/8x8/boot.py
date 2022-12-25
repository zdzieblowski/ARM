from libs import Neopixel
import utime
import math

matrix_size = 64
matrix_w = 8

matrix = Neopixel(matrix_size, 0, 15, "GRB", matrix_w, 0)
matrix.brightness(2)

# 

matrix.mClear()
utime.sleep(.5)

# CORNER TEST

matrix.mSetPixel(0,0,(255,255,255))
matrix.mSetPixel(7,0,(255,255,255))
matrix.mSetPixel(0,7,(255,255,255))
matrix.mSetPixel(7,7,(255,255,255))
matrix.show()
utime.sleep(5)

matrix.mClear()
utime.sleep(.5)

# COLOR TEST

colors = []
for p in range(0, matrix_size):
    colors.append(matrix.colorHSV(p*1024,255,255))

temp_time = utime.time()

while temp_time > utime.time()-5:
    matrix.mDrawData(colors)
 
    temp = colors[0]
    colors.pop(0)
    colors.append(temp)

matrix.mClear()
