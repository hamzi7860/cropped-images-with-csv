import csv
from io import BytesIO
import requests
from PIL import Image
import matplotlib.pyplot as plt

#im = Image.open(r"D:/Urooj/New_Conversion/New_Conversion/E5/")

# open file to read
with open("labels.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
   

    # iterate on all lines
    i = 0
    for line in csvfile:
        splitted_line = line.split(',')
        # check if we have an image URL
        if splitted_line[0] != '' and splitted_line[0] != "\n":
            #response = requests.get(splitted_line[1])
            img = Image.open(r"C:/Users/Hamza Chaudhary/Desktop/cropped/Imagesfilename/"+splitted_line[0])

            #im.crop(box) ⇒ 4-tuple defining the left, upper, right, and lower pixel coordinate
            left_x = int(splitted_line[1])
            top_y = int(splitted_line[2])
            right_x = int(splitted_line[3])
            bottom_y = int(splitted_line[4])
            crop = img.crop((left_x, top_y, right_x, bottom_y))
            new_img = crop.resize((256, 256))
            """ 
            # preview new images
            imgplot = plt.imshow(new_img)
            plt.show()
            """
            new_img.save(str(i) + ".jpg")
            print("Image saved for {0}".format(splitted_line[0]))
            i += 1
        else:
            print("No result for {0}".format(splitted_line[0]))
