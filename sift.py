import cv2
import numpy as np
import utils
from sklearn.externals import joblib
from sklearn import svm
from sklearn import datasets

dir='/Users/xiangkui/workspace/tsinghua_exp/src/main/resource/demo'
target = '/Users/xiangkui/workspace/tsinghua_exp/target'
bow_dir=target+"/bow";
sift = cv2.SIFT()
# kp = sift.detect(gray,None)
# img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imwrite(dir+'/sift_keypoints.jpg',img)
training_paths=utils.GetFileList(dir,[])
descriptors = []
for path in training_paths:
    print path
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    kp, dsc= sift.detectAndCompute(gray, None)
    descriptors.append(dsc)

des = np.array(descriptors)
k=10
bow = cv2.BOWKMeansTrainer(k)
result = bow.cluster(des)

print result.size


#
# joblib.dump(des, bow_dir+'/bow.pkl')
#
# svm_dir=target+'/svm'
# clf = svm.SVC()
#
#
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
# clf.fit(X, y)
# joblib.dumps(clf,svm_dir+'/svm.pkl')
#
# clf.predict(T)



