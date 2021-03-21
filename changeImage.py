import argparse
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)


# fake = glob.glob("Fake/*.png")
# real = glob.glob("Real/*.png")

parser = argparse.ArgumentParser()
parser.add_argument("s")
parser.add_argument("d")
args = parser.parse_args()
print(args.d)

sourceFld = glob.glob(args.s)
print(sourceFld)
desFld = args.d
print(desFld)

# print(sourceFld)
for file in sourceFld:
    colored = cv2.imread(file)
    # Important line to change======================should be dynamic
    sp = file.split("\\")[5]
    # print(sp)
    # plt.imshow(colored)
    # plt.show()
    colored = cv2.cvtColor(colored, cv2.COLOR_BGR2LUV)
    # plt.imshow(colored)
    # plt.show()
    # cv2.imshow('image', colored)
    # cv2.waitKey(0)
    cv2.imwrite('{}/{}'.format(desFld, sp), colored)
