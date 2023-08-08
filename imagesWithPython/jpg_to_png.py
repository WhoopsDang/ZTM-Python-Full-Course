import sys
import os
from PIL import Image

# Target folder
pokedex = sys.argv[1]
new = sys.argv[2]

# check if new exists
if not os.path.exists(new):
    os.makedirs(new)

for filename in os.listdir(pokedex):
    img = Image.open(pokedex + filename)
    print(f"Saving {filename[:-3]}png")
    img.save(new + filename[:-3] + "png")
