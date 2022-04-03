import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def get_color(pixel):
    colors = [np.array((109, 0, 26)),
              np.array((190, 0, 57)),
              np.array((255, 69, 0)),
              np.array((255, 168, 0)),
              np.array((255, 214, 53)),
              np.array((255, 248, 184)),
              np.array((0, 163, 104)),
              np.array((0, 204, 120)),
              np.array((126, 237, 86)),
              np.array((0, 117, 111)),
              np.array((0, 158, 170)),
              np.array((0, 204, 192)),
              np.array((36, 80, 164)),
              np.array((54, 144, 234)),
              np.array((81, 233, 244)),
              np.array((73, 58, 193)),
              np.array((106, 92, 255)),
              np.array((148, 179, 255)),
              np.array((129, 30, 159)),
              np.array((180, 74, 192)),
              np.array((228, 171, 255)),
              np.array((222, 16, 127)),
              np.array((255, 56, 129)),
              np.array((255, 153, 170)),
              np.array((109, 72, 47)),
              np.array((156, 105, 38)),
              np.array((255, 180, 112)),
              np.array((0, 0, 0)),
              np.array((81, 82, 82)),
              np.array((137, 141, 144)),
              np.array((212, 215, 217)),
              np.array((255, 255, 255))
             ]
    min_dist = 999999
    min_idx = 0
    for i in range(len(colors)):
        if sum( np.abs(pixel - colors[i])) < min_dist:
            min_idx = i
            min_dist = sum( np.abs(pixel - colors[i]))
            
    return colors[min_idx]

def generate_pixart(sizex,sizey):
    image = Image.open("image.jpg")
    image_resized = image.resize((sizex,sizey))
    image_resized = np.array(image_resized)
    new_image = image_resized.copy()
    for i in range(image_resized.shape[0]):
        for j in range(image_resized.shape[1]):
            pixel = image_resized[i,j,:]
            new_pixel = get_color(pixel)
            new_image[i,j] = new_pixel
    plt.imsave("output_image.png",new_image)

    x = int(input("enter image width"))
    y = int(input("enter image height"))
    generate_pixart(300,300)