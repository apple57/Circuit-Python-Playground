import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    # indexes the first element of the 'pixels' list and points to the 
    # first (and only) Neopixel in the 'pixels' list
    pixels[0]=(0, 255, 0)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
