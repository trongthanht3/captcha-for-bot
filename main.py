import cv2
import numpy as np

path = 'data/1605371875692.jpg'
img = cv2.imread(path, 0)
x0, y0 = img.shape

img_ori = cv2.imread(path)
img = cv2.resize(img, (y0 * 2, x0 * 2))
img_ori = cv2.resize(img_ori, (y0 * 2, x0 * 2))

arr = np.ones(img.shape, dtype=np.uint8) * 0
arr1 = np.ones(img.shape, dtype=np.uint8) * 255
print(arr.shape)
print(img.shape)
img_not = cv2.bitwise_not(img, arr)

kernel = np.array([[0, -5, 0],
                   [-5, 20, -5],
                   [0, -5, 0]])

img_not = cv2.filter2D(img_not, -1, kernel)

kernel_denoise = np.ones((3, 3), np.uint8)

cv2.dilate(img_not, kernel_denoise, img_not, iterations=1)
cv2.threshold(img_not, 127, 255, cv2.THRESH_BINARY_INV, img_not)

x_min = -1
x_max = 0
x0, y0 = img_not.shape

for x in range(0, y0):
    for y in range(0, x0):
        if img_not[y, x] == 0:
            if x_min == -1:
                x_min = x
            x_max = x
        # print(x0,y0)

print(x_min, x_max)

y_min = int(x0 * 0.15)
y_max = int(x0 * 0.85)
# cv2.imshow('1', img_not[y_min:y_max, x_min:x_max])
img_new = img_not[y_min:y_max, x_min:x_max]
y, x = img_new.shape


# cut = 6

def split_image(cut):
    dis = int((x_max - x_min) / cut)
    for i in range(cut):
        cv2.imwrite("cache/" + str(cut) + "_" + str(i) + ".jpg", img_not[y_min:y_max, dis * i:dis * (i + 1)])


split_image(8)
split_image(7)
split_image(6)
split_image(5)
split_image(4)

# cv2.waitKey()
