# import cv2
# import numpy as np
#
# # Load the image
# image = cv2.imread('image.jpg', 0)
#
# # Threshold the image to obtain a binary image
# ret, thresh = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)
#
# # Find contours
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Iterate through the contours and find the coordinates of the bounding box of the black square
# for contour in contours:
#     x, y, w, h = cv2.boundingRect(contour)
#     if abs(w-h) < 2:  # Assuming the black square is a perfect square
#         print("Coordinates of the black square: x={}, y={}, width={}, height={}".format(x, y, w, h))


from PIL import Image

img = Image.open('image.jpg').convert('1')
pixels = img.load()

xlist = []
ylist = []
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixels[x, y] == 0:
            xlist.append(x)
            ylist.append(y)

#4 corners of the black square
xleft = min(xlist)
xright = max(xlist)
ytop = min(ylist)
ybot = max(ylist)
print(abs(xleft - xright), abs(ytop - ybot))