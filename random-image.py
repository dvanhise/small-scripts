from PIL import Image
import os

height = 500
width = 500
Image.frombytes('RGB', (width, height), os.urandom(height*width*3)).show()
