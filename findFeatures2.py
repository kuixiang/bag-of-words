#!/usr/local/bin/python2.7
import argparse as ap
import cv2
import numpy as np
import os
import utils
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from scipy.cluster.vq import *
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':
    # Get the path of the training set
    parser = ap.ArgumentParser()
    parser.add_argument("-t", "--trainingSet", help="Path to Training Set", required="True")
    parser.add_argument("-l", "--label", help="a file of record Training Set info.", required="True")
    args = vars(parser.parse_args())
    # Get the training classes names and store them in a list
    train_path = args["trainingSet"]

    label_file = args["label"]
    dict=utils.readDict(label_file)
    # get training_names
    training_names=list(set(dict.values()))

    image_paths = []
    image_classes = []
    class_id = 0
    dir = os.path.join(train_path)
    image_paths=[]
    image_paths=utils.getFileList(dir,"JPEG",image_paths)

    #sample datas
    image_paths=utils.RandomSampling(image_paths,len(image_paths)/10);


    for image in image_paths:
        names=image.split('/')
        name=names[len(names)-1].split('.')[0]
        image_classes.append(dict[name])

    # Create feature extraction and keypoint detector objects
    fea_det = cv2.FeatureDetector_create("SIFT")
    des_ext = cv2.DescriptorExtractor_create("SIFT")
    # List where all the descriptors are stored
    print "List where all the descriptors are stored"
    des_list = []
    count=0
    for image_path in image_paths:
        progress=100*(1.0*count)/len(image_paths)
        progress=float('%0.1f'%progress)
        im = cv2.imread(image_path)
        kpts = fea_det.detect(im)
        kpts, des = des_ext.compute(im, kpts)
        des_list.append((image_path, des))
        count+=1
        print "image_path:"+image_path+",process :"+str(progress)+"%"

    # Stack all the descriptors vertically in a numpy array
    descriptors = des_list[0][1]
    for image_path, descriptor in des_list[1:]:
        descriptors = np.vstack((descriptors, descriptor))


    # Perform k-means clustering
    print "start to perform k-means clustering..."
    k = 100
    voc, variance = kmeans(descriptors, k, 1)

    # Calculate the histogram of features
    print "Calculate the histogram of features ..."
    im_features = np.zeros((len(image_paths), k), "float32")
    for i in xrange(len(image_paths)):
        words, distance = vq(des_list[i][1],voc)
        for w in words:
            im_features[i][w] += 1

    # Perform Tf-Idf vectorization
    print "Perform Tf-Idf vectorization"
    nbr_occurences = np.sum( (im_features > 0) * 1, axis = 0)
    idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')

    # Scaling the words
    print "Scaling the words"
    stdSlr = StandardScaler().fit(im_features)
    im_features = stdSlr.transform(im_features)

    # Train the Linear SVM
    print "Train the Linear SVM"
    clf = LinearSVC()
    clf.fit(im_features, np.array(image_classes))

    # Save the SVM
    print "Save the SVM"
    joblib.dump((clf, training_names, stdSlr, k, voc), "bof.pkl", compress=3)
