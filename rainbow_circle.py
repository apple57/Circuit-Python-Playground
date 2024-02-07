import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    for pixel in range(10):
        pixels[pixel]=(0, 250 - pixel*25, pixel*25)
        time.sleep(0.1)
        pixels.fill((0,0,0,))
    for pixel in range(10):
        pixels[pixel]=(pixel*25, 0, 250-pixel*25)
        time.sleep(0.1)
        pixels.fill((0,0,0))
    for pixel in range(10):
        pixels[pixel]=(250-pixel*25, pixel*25, 0)
        time.sleep(0.1)
        pixels.fill((0,0,0))