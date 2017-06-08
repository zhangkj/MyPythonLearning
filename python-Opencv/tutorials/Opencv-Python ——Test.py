#***test


import cv2
import numpy as np

img3 = np.random.random((600, 800, 3))

while 1:
    img3 = np.random.random((600, 800, 3))
    img3 *= 50
    img3 = img3.round()

    cv2.imshow('img',img3)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()