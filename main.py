import cv2
import numpy as np

img = cv2.imread('goc.jpg', 0)
x0, y0 = img.shape

img_ori = cv2.imread('goc.jpg')
img = cv2.resize(img, (y0 * 2, x0 * 2))
img_ori = cv2.resize(img_ori, (y0 * 2, x0 * 2))

arr = np.ones(img.shape, dtype=np.uint8) * 0
arr1 = np.ones(img.shape, dtype=np.uint8) * 255
print(arr.shape)
print(img.shape)
img_not = cv2.bitwise_not(img, arr)

# img_xor = cv2.bitwise_and(img, arr1)
# img = cv2.resize(img,(320,120))
# img_ori = cv2.resize(img_ori,(320,120))

# edge = cv2.Canny(img, 100, 100)
# contours, h = cv2.findContours(edge, 1, 2)
# for idx, con in enumerate(contours):
#     x, y, w, h = cv2.boundingRect(con)
#     if cv2.contourArea(con) < 100000:
#         # cv2.drawContours(img_ori, contours, idx, (0, 255, 0), 1)
#         cv2.rectangle(img_ori, (x, y), (x + w, y + h), (0, 255, 0), 1)

kernel = np.array([[0, -5, 0],
                   [-5, 20, -5],
                   [0, -5, 0]])
kernel_denoise = np.ones((2,2), np.uint8)
kernel_denoise2 = np.ones((1,1), np.uint8)
img_not = cv2.filter2D(img_not, -1, kernel)

# # erosion = cv.erode(img,kernel,iterations = 1)
#
# cv2.medianBlur(img_not, 3, img_not)

cv2.dilate(img_not, kernel_denoise, img_not, iterations=1)
# img_not = cv2.morphologyEx(img_not, cv2.MORPH_OPEN, kernel_denoise2)
# img_not = cv2.medianBlur(img_not,3) #3
cv2.threshold(img_not, 127, 255, cv2.THRESH_BINARY_INV, img_not)

xmin = -1;
xmax = 0;
x0, y0 = img_not.shape

for x in range(0, y0):
    for y in range(0, x0):
        if img_not[y, x] == 0:
            if xmin == -1:
                xmin = x
            xmax = x
        # print(x0,y0)

print(xmin, xmax)
# img_not = cv2.cvtColor(img_not,cv2.COLOR_GRAY2BGR)
# dst = cv2.fastNlMeansDenoisingColored(img_not,None,10,10,7,21)

# edge = cv2.Canny(img_not, 100, 100)
# for i in range(0,1):
#     contours, h = cv2.findContours(img_not, 1, 2)
#     for idx, con in enumerate(contours):
#         x, y, w, h = cv2.boundingRect(con)
#         if cv2.contourArea(con) < 10000:
#             cv2.drawContours(img_not, contours, idx, (0, 255, 0), 1)
#             cv2.rectangle(img_not, (x, y), (x + w, y + h), (0, 255, 0), 1)

# contours, h = cv2.findContours(img_not, 1, 2)
# for idx, con in enumerate(contours):
#     x, y, w, h = cv2.boundingRect(con)
#     if cv2.contourArea(con) < 10000:
#         cv2.rectangle(img_not, (x, y), (x + w, y + h), (0, 255, 0), 1)
ymin = int(x0 * 0.15)
ymax = int(x0 * 0.85)
cv2.imshow('1', img_not[ymin:ymax, xmin:xmax])
img_new = img_not[ymin:ymax, xmin:xmax]
y, x = img_new.shape

# cut ảnh với số mẫu 4-8
for cut in range(4,9):
    dis = int((xmax - xmin) / cut)
    for i in range(cut):
        cv2.imshow('cache/' + str(cut) + '_' + str(i) + ".jpg", img_new[:, dis * i:dis * (i + 1)])
        cv2.imwrite('cache/' + str(cut) + '_' + str(i) + ".jpg", img_new[:, dis * i:dis * (i + 1)])
cv2.imshow('2', img_not)

# cv2.imwrite('anh.jpg', img_not)


cv2.waitKey()
