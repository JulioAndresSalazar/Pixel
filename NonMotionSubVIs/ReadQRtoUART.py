# Constantly searching/reading QR code, any time code read value is sent to Rio

# Import nescesary libraries
import sensor, image, time, sys, utime
from pyb import UART

# reset the sensors of the camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must turn this off to prevent image washout...
clock = time.clock()

# Initialize UART connection
uart = UART(3, 9600, timeout_char=1000)
uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000) # init with given parameters

while(True):
   clock.tick()
   img = sensor.snapshot()
   img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
   for code in img.find_qrcodes():
       img.draw_rectangle(code.rect(), color = (255, 0, 0))
       input=code.payload()
       input=input+'\n'
       uart.write(input)
       print(input)
       utime.sleep(10)



