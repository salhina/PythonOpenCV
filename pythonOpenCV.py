#!/usr/bin/env python

import numpy as np

import cv2

img = cv2.imread('pythonOpenCV.png')

cv2.imshow('My photo', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

#cv2.destroyAllWindows()
