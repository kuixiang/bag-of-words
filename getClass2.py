#!/usr/local/bin/python2.7

import argparse as ap
import cv2
import numpy as np
import os
from sklearn.externals import joblib
from scipy.cluster.vq import *
import utils

# Load the classifier, class names, scaler, number of clusters and vocabulary 
clf, classes_names, stdSlr, k, voc = joblib.load("bof.pkl")


# Get the path of the testing set
parser = ap.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--testingSet", help="Path to testing Set")
group.add_argument("-i", "--image", help="Path to image")
parser.add_argument("-l", "--label", help="a file of record Training Test info.", required="True")
args = vars(parser.parse_args())

# Get the path of the testing image(s) and store them in a list
image_paths = []
if args["testingSet"]:
    test_path = args["testingSet"]
    try:
        dir = test_path
    except OSError:
        print "No such directory {}\nCheck if the file exists".format(test_path)
        exit()
    image_paths=[]
    image_paths=utils.getFileList(dir,"JPEG",image_paths)

else:
    image_paths = [args["image"]]

#image_paths=image_paths[:len(image_paths)/10]

image_paths=utils.RandomSampling(image_paths,len(image_paths)/100);


# Create feature extraction and keypoint detector objects
fea_det = cv2.FeatureDetector_create("SIFT")
des_ext = cv2.DescriptorExtractor_create("SIFT")

# List where all the descriptors are stored
des_list = []

for image_path in image_paths:
    im = cv2.imread(image_path)
    if im==None:
        print "No such file {}\nCheck if the file exists".format(image_path)
        exit()
    kpts = fea_det.detect(im)
    kpts, des = des_ext.compute(im, kpts)
    des_list.append((image_path, des))   

# Stack all the descriptors vertically in a numpy array
descriptors = des_list[0][1]
for image_path, descriptor in des_list[0:]:
    descriptors = np.vstack((descriptors, descriptor)) 

# 
test_features = np.zeros((len(image_paths), k), "float32")
for i in xrange(len(image_paths)):
    words, distance = vq(des_list[i][1],voc)
    for w in words:
        test_features[i][w] += 1

# Perform Tf-Idf vectorization
nbr_occurences = np.sum( (test_features > 0) * 1, axis = 0)
idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')

# Scale the features
test_features = stdSlr.transform(test_features)

# Perform the predictions
predictions = []
for i in clf.predict(test_features):
    predictions.append(i)

label_file = args["label"]
dict=utils.readDict(label_file)


count=0
total=len(zip(image_paths, predictions))
for image_path, prediction in zip(image_paths, predictions):
    print image_path,prediction,dict[utils.getFileName(image_path)]
    if(prediction==dict[utils.getFileName(image_path)]):
        count+=1

print "total: "+str(total)
print "accuracy: "+str((1.0*count/total*100))+"%"

