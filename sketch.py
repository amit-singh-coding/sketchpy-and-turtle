#sketchpy using inbuilt image........
# from sketchpy import library as lib
# obj = lib.flag()
# obj.draw()

#sketchpy using randam image from PC.....
from sketchpy import canvas
obj=canvas.sketch_from_image(r'C:\Users\royal\Desktop\Project\image.jpg')
obj.draw(threshold=125)

