import os
import struct
import random
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

def getFileName(image):
    names=image.split('/')
    name=names[len(names)-1].split('.')[0]
    return name
def typeList():
    return {
        "FFD8FF": "JPEG",
        "89504E47": "PNG"}
def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()
def filetype(filename):
    binfile = open(filename, 'rb')
    tl = typeList()
    ftype = 'unknown'
    for hcode in tl.keys():
        numOfBytes = len(hcode) / 2
        binfile.seek(0)
        hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes))
        f_hcode = bytes2hex(hbytes)
        if f_hcode == hcode:
            ftype = tl[hcode]
            break
    binfile.close()
    return ftype

def getFileList(dir,type,fileList):
    newDir = dir
    if os.path.isfile(dir) and filetype(dir)==type:
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            getFileList(newDir, type,fileList)
    return fileList


def loadDataSet(fileName):	  #general function to parse tab -delimited floats
    dataMat = []				#assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        #		 fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(curLine)
    return dataMat

def RandomSampling(dataMat,number):
    try:
        slice = random.sample(dataMat, number)
        return slice
    except:
        print 'sample larger than population'

def RepetitionRandomSampling(dataMat,number):
    sample=[]
    for i in range(number):
        sample.append(dataMat[random.randint(0,len(dataMat)-1)])
    return sample
def SystematicSampling(dataMat,number):

    length=len(dataMat)
    k=length/number
    sample=[]
    i=0
    if k>0 :
        while len(sample)!=number:
            sample.append(dataMat[0+i*k])
            i+=1
        return sample
    else:
        return RandomSampling(dataMat,number)

def readDict(label_file):
    dict={}
    read = open(label_file)
    while True:
        line = read.readline()
        if len(line)==0:
            break
        lineStr=line.split(' ')
        dict[lineStr[0]]=lineStr[1].strip()
    read.close
    return dict

#if __name__=='__main__':
#    dataMat=loadDataSet('/Users/hakuri/Desktop/data1.txt')
    #	print RandomSampling(dataMat,7)
    #	RepetitionSampling(dataMat,4)
#    print SystematicSampling(dataMat,9)


