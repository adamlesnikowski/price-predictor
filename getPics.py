#Get AirBnB photos script
#Optionally run interactively in iPython, Jupyter and examine the db data frame or call getData(0, howeverManyImages)

import sys
import os
import pandas as pd
import numpy
import urllib
import time

#City to read listings file from. In this case Paris.
#Set read_csv_loc as location of where you downloaded and unpacked /data/listings.csv.gz
read_csv_loc = '/home/adam/CVProjects/AirBnBConvNet/Data/PAR/listingsBig.csv'
#Set out_image_base to wherever you want the image data to go
out_image_base = '/home/adam/CVProjects/AirBnBConvNet/Data/Pics/PAR/'

#pandas work
db = pd.read_csv(read_csv_loc)
print(db.keys())
urls = db['xl_picture_url']
dict = urls.to_dict()
values = dict.values()
length = len(values)

def getData(start, end):
    for i in xrange(start, end):
        delay =  abs(numpy.random.randn()) #samples from normal with mean 0, variance 1
        time.sleep(delay)
        print("Delayed for %s seconds" % delay)
        try:
            link = values[i]
            id = db.id[i]
            out_image_location = out_image_base + str(id) + '.jpg'
            urllib.urlretrieve(link, out_image_location)
            print("Got image %s" % id)
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s </p>" % e )

#Get all the data!
getData(0, length)
