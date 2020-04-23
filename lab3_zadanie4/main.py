from argparse import ArgumentParser
from my_mod import display
from my_mod import bordering
from my_mod import labeling
from my_mod import gaussian_blur
from my_mod import affine_transformation
from my_mod import rotate
import cv2 as cv
import time
import datetime


def main():
    parser = ArgumentParser(
        description='INSERT path to image you want to change, and path where to save changed image'
                    'EXAMPLE: python3 main.py /home/adam/Python1/lab_3_zadanie_4/starry_night.jpg '
                    '/home/adam/Python1/lab_3_zadanie_4/starry_night_new.jpg')
    parser.add_argument('filepath1')
    parser.add_argument('filepath2')
    args = parser.parse_args()


    labeling(args.filepath1, args.filepath2)
    bordering(args.filepath2, args.filepath2)
    gaussian_blur(args.filepath2, args.filepath2)
    rotate(args.filepath2, args.filepath2)
    affine_transformation(args.filepath2, args.filepath2)
    gaussian_blur(args.filepath2, args.filepath2)
    gaussian_blur(args.filepath2, args.filepath2)
    rotate(args.filepath2, args.filepath2)
    display(args.filepath2)



if '__main__' == __name__:
    start_time = time.time()
    main()


    conversion = datetime.timedelta(seconds=(time.time() - start_time))
    print("--- time: %s ---" % conversion)