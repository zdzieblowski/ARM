from libs import Neopixel
import utime
import math

matrix_size = 64
matrix_width = 8
matrix_brightness = 16

matrix = Neopixel(matrix_size, 0, 15, "GRB", matrix_width, 0)
matrix.brightness(matrix_brightness)

# Methods

def run(func, func_pause = 0):
    func(func_pause)
    matrix.mClear()
    utime.sleep(.5)

# Algorithms

def cornerTest(pause):
    matrix.mSetPixel(0,0,(255,255,255))
    matrix.mSetPixel(7,0,(255,255,255))
    matrix.mSetPixel(0,7,(255,255,255))
    matrix.mSetPixel(7,7,(255,255,255))
    matrix.show()
    utime.sleep(pause)

def colorTest(pause):
    colors = []

    for p in range(0, matrix_size):
        colors.append(matrix.colorHSV(p*1024,255,255))

    temp_time = utime.time()

    while temp_time > utime.time()-pause:
        matrix.mDrawData(colors)

        temp = colors[0]
        colors.pop(0)
        colors.append(temp)

def brightnessTest(pause):
    grays = []
    for p in range(0, matrix_size):
        grays.append((p*4,p*4,p*4))

    matrix.mDrawData(grays)
    utime.sleep(pause)

# Run

run(cornerTest, 2)
run(colorTest, 2)
run(brightnessTest, 2)
