##***Getting Started with Images
#Learn to load an image, display it and save it back

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('messi5.jpg', 0)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Write an Image
cv2.imwrite('messigray.png',img)


# #---------Using Matplotlib
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread('messi5.jpg',0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()