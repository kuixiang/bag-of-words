# from pandas_confusion import ConfusionMatrix
from nltk.metrics.confusionmatrix import ConfusionMatrix

def confusion(targets,outputs):
    numClasses = len(outputs)
    numSamples = len(targets[0])

    for col in range(numSamples):
        max = outputs[0][col]
        ind = 0
        for row in range(numClasses):
            if outputs[row][col] > max:
                max = outputs[row][col]
                ind = row
                
            outputs[row][col] = 0.0
            
        outputs[0][col] = 0.0
        outputs[ind][col] = 1

    count = 0

    for row in range(numClasses):
        for col in range(numSamples):
            if(targets[row][col] != outputs[row][col]):
                count+=1

    c = 1.0*count/(2*numSamples)

    cm=[[0 for x in range(numClasses)] for y in range(numClasses)]
    for row in range(numClasses):
        for col in range(numClasses):
            cm[row][col] = 0

    i=[0 for x in range(numSamples)]
    j=[0 for x in range(numSamples)]

    for col in range(numSamples):
        for row in range(numClasses):
            if(targets[row][col]==1.0):
                i[col] = row
                break

    for col in range(numSamples):
        for row in range(numClasses):
            if (outputs[row][col]==1.0):
                j[col] = row
                break

    for col in range(numSamples):
        cm[i[col]][j[col]] = cm[i[col]][j[col]] + 1

    ind=[[0 for x in range(numClasses)] for y in range(numClasses)]

    for row in range(numClasses):
        for col in range(numClasses):
            ind[row][col] = ""

    for col in range(numSamples):
        if(ind[i[col]][j[col]]==""):
            ind[i[col]][j[col]] = str(col)
        else:
            ind[i[col]][j[col]] = str(ind[i[col]][j[col]])+","+str(col)


    # Percentages
    per=[[0 for x in range(4)] for y in range(numClasses)]
    for row in range(numClasses):
        for col in range(4):
            per[row][col] = 0.0

    for row in range(numClasses):
        yi=[0 for x in range(numSamples)]
        ti=[0 for x in range(numSamples)]
        for col in range(numSamples):
            yi[col] = outputs[row][col]
            ti[col] = targets[row][col]
        a = 0
        b = 0
        for col in range(numSamples):
            if ((yi[col] != 1) and ti[col] == 1):
                a = a + 1
            if (yi[col] != 1):
                b = b + 1
        per[row][0] = 1.0*a/b
        a = 0
        b = 0

        for col in range(numSamples):
            if ((yi[col] == 1) and (ti[col]!=1)):a = a + 1
            if (yi[col] == 1):b = b + 1

        per[row][1] = 1.0*a/b
        a = 0
        b = 0
        for col in range(numSamples):
            if ((yi[col] == 1) and ti[col] == 1) :a = a + 1
            if (yi[col] == 1) :b = b + 1

        per[row][2] = 1.0*a/b
        a = 0
        b = 0
        for col in range(numSamples):
            if ((yi[col] != 1) and ti[col] != 1) :a = a + 1
            if (yi[col] != 1): b = b + 1
        per[row][3] = 1.0*a/b

    # //NAN handling
    for row in range(numClasses):
        for col in range(4):
            if (per[row][col] is None):
                per[row][col] = 0.0

    return [round(c, 2),cm,ind,per]


class Confusion(object):
    c=""
    cm=""
    ind=""
    per=""
    def __init__(self):
        pass

class Out(object):
    confusion = Confusion()
    avgAccuracy = 0.0
    errRate = 0.0
    precisionMicro = 0.0
    recallMicro = 0.0
    fscoreMicro = 0.0
    precisionMacro = 0.0
    recallMacro = 0.0
    fscoreMacro = 0.0
    def __init__(self):
        pass

def evaluation(targets,outputs):
    # cm=ConfusionMatrix(targets,outputs)
    [c,cm,ind,per] = confusion(targets,outputs)
    out = Out()
    out.confusion.c = c
    out.confusion.cm = cm
    out.confusion.ind = ind
    out.confusion.per = per
    return out
    #Average Accuracy (The average per-class effectiveness of a classifier)
    nClasses=len(outputs)
    avgAccuray=0.0

    for i in nClasses:
        fn=per(i,1)
        fp=per(i,2)
        tp=per(i,3)
        tn=per(i,4)
        avgAccuray=+avgAccuray+((tp+tn)/(tp+fn+fp+tn))

    avgAccuray=avgAccuray/nClasses

    #Error Rate (The average per-class classification error)
    errRate=0.0


    for i in range(nClasses):
        fn=per(i,0)
        fp=per(i,1)
        tp=per(i,2)
        tn=per(i,3)
        errRate=+errRate+((fp+fn)/(tp+fn+fp+tn))

    errRate=errRate/nClasses

    #Precision-Micro (Agreement of the data class labels with those of a
    #classifiers if calculated from sums of per-text decisions)
    numerator=0.0
    denominator=0.0

    for i in nClasses:
        fn=per(i,0)
        fp=per(i,1)
        tp=per(i,2)
        tn=per(i,3)
        numerator=numerator+tp
        denominator=denominator+ (tp+fp)

    precisionMicro=numerator/denominator

    #Recall-Micro (Effectiveness of a classifier to identify class labels if
    #calculated from sums of per-text decisions)
    numerator=0.0
    denominator=0.0
    for i in nClasses:
        fn=per(i,0)
        fp=per(i,1)
        tp=per(i,2)
        tn=per(i,3)
        numerator=numerator+tp
        denominator=denominator+ (tp+fn)

    recallMicro=numerator/denominator

    beta=1
    numerator=(beta^2+1)*precisionMicro*recallMicro
    denominator=beta^2*precisionMicro+recallMicro
    fscoreMicro=numerator/denominator

    #-------------------------------------------------------
     #Precision-Macro (An average per-class agreement of the data class labels with those of a classifiers)
    precisionMacro=0.0

    for i in nClasses:
        fn=per(i,0)
        fp=per(i,1)
        tp=per(i,2)
        tn=per(i,3)
        precisionMacro=precisionMacro+(tp/(tp+fp))

    precisionMacro=precisionMacro/nClasses

    #Recall-Micro (An average per-class effectiveness of a classifier to identify class labels)
    recallMacro=0.0

    for i in nClasses:
        fn=per(i,0)
        fp=per(i,1)
        tp=per(i,2)
        tn=per(i,3)
        recallMacro=recallMacro+(tp/(tp+fn))

    recallMacro=recallMacro/nClasses

    beta=1
    numerator=(beta^2+1)*precisionMacro*recallMacro
    denominator=beta^2*precisionMacro+recallMacro
    fscoreMacro=numerator/denominator

    out.avgAccuracy = avgAccuray*100
    out.errRate = errRate*100
    out.precisionMicro = precisionMicro*100
    out.recallMicro = recallMicro*100
    out.fscoreMicro = fscoreMicro*100

    out.precisionMacro = precisionMacro*100
    out.recallMacro = recallMacro*100
    out.fscoreMacro = fscoreMacro*100
    return out
