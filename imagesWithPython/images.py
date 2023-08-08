from PIL import Image, ImageFilter

# img = Image.open("./Pokedex/pikachu.jpg")

# indicates the filetype
# img.format

# indicates filesize
# img.size

# indicates colortype
# img.mode

# Passes an image throug a blur effect
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", "png")

# Passes an image throug a smoothing effect
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save("blur.png", "png")

# use img.convert to convert it to different image formats
# user img() with a degree parameter to raotate the image
# use resize() with dimension parameters to scale the image. Parameter must be passed as a tuple


img = Image.open("./astro.jpg")
img.thumbnail((400, 400))

img.save("thumbnail.jpg")
