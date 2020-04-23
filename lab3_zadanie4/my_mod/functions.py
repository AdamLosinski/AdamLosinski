import cv2 as cv
from cv2 import rotate, ROTATE_90_CLOCKWISE
import sys
import numpy as np
    

def display(image_path):
    img = cv.imread(image_path)
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)

def bordering(image_path, new_image_path):
    img = cv.imread(image_path)
    if img is None:
        sys.exit("Could not read the image.")
    reflect = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT)
    #cv.imshow("Bordered image", img)
    cv.imwrite(new_image_path, reflect)

def labeling(image_path, new_image_path):
    img = cv.imread(image_path)
    logo = cv.imread('opencv-logo-white.png')
    if img is None:
        sys.exit("Could not read the image.")
    if logo is None:
        sys.exit("Could not read the logo.")
    logo = cv.resize(logo,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
    rows,cols,channels = logo.shape
    roi = img[0:rows, 0:cols]
    logogray = cv.cvtColor(logo,cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(logogray, 10,255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)
    img_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
    logo_fg = cv.bitwise_and(logo,logo,mask = mask)
    dst = cv.add(img_bg, logo_fg)
    img[0:rows, 0:cols ] = dst
    cv.imwrite(new_image_path, img)

def gaussian_blur(image_path, new_image_path):
    img = cv.imread(image_path)
    if img is None:
        sys.exit("Could not read the image.")
    blur = cv.GaussianBlur(img,(5,5),0)
    cv.imwrite(new_image_path, blur)

def affine_transformation(image_path, new_image_path):
    img = cv.imread(image_path)
    if img is None:
        sys.exit("Could not read the image.")
    rows,cols,ch = img.shape
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv.getAffineTransform(pts1,pts2)
    dst = cv.warpAffine(img,M,(cols,rows))
    cv.imwrite(new_image_path, dst)

def rotate(image_path, new_image_path):
    img = cv.imread(image_path)
    if img is None:
        sys.exit("Could not read the image.")
    rows,cols,ch = img.shape
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    dst = cv.warpAffine(img,M,(cols,rows))
    cv.imwrite(new_image_path, dst)


