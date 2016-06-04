package com.deepsenselab.accuracy_evaluation;

/**
 * Created by Ashok K. Pant (ashokpant87@gmail.com) on 3/17/16.
 */
public class Evaluation {
    private double avgAccuray;
    private double errRate;
    private double precisionMicro;
    private double recallMicro;
    private double fscoreMicro;
    private double precisionMacro;
    private double recallMacro;
    private double fscoreMacro;

    Evaluation() {
        avgAccuray = 0.0;
        errRate = 0.0;
        precisionMicro = 0.0;
        recallMicro = 0.0;
        fscoreMicro = 0.0;
        precisionMacro = 0.0;
        recallMacro = 0.0;
        fscoreMacro = 0.0;
    }

    Evaluation(Confusion confusion) {
        avgAccuray = 0.0;
        errRate = 0.0;
        precisionMicro = 0.0;
        recallMicro = 0.0;
        fscoreMicro = 0.0;
        precisionMacro = 0.0;
        recallMacro = 0.0;
        fscoreMacro = 0.0;
        evaluation(confusion);
    }

    public void evaluation(Confusion confusion){
        double[][] per =confusion.getPer();
        int numClasses=confusion.getClasses();

        //Average Accuracy (The average per-class effectiveness of a classifier)
        double avgAccuracy=0.0;
        double fn=0.0,fp=0.0,tp=0.0,tn=0.0;
        for (int i=0;i<numClasses;i++){
            fn=per[i][0];
            fp=per[i][1];
            tp=per[i][2];
            tn=per[i][3];
            avgAccuracy=+avgAccuracy+((tp+tn)/(tp+fn+fp+tn));
        }
        avgAccuracy=avgAccuracy/numClasses;

        //Error Rate (The average per-class classification error)
        double errRate=0.0;
        for (int i=0;i<numClasses;i++){
            fn=per[i][0];
            fp=per[i][1];
            tp=per[i][2];
            tn=per[i][3];
            errRate=+errRate+((fp+fn)/(tp+fn+fp+tn));
        }
        errRate=errRate/numClasses;

        //Precision-Micro (Agreement of the data class labels with those of a classifiers if calculated from sums of per-text decisions)
        double  numerator=0.0;
        double  denominator=0.0;
        for (int i=0;i<numClasses;i++){
            fn=per[i][0];
            fp=per[i][1];
            tp=per[i][2];
            tn=per[i][3];
            numerator=numerator+tp;
            denominator=denominator+ (tp+fp);
        }
        double    precisionMicro=numerator/denominator;

        //Recall-Micro (Effectiveness of a classifier to identify class labels if calculated from sums of per-text decisions)
        numerator=0.0;
        denominator=0.0;
        for (int i=0;i<numClasses;i++){
            fn=per[i][0];
            fp=per[i][1];
            tp=per[i][2];
            tn=per[i][3];
            numerator=numerator+tp;
            denominator=denominator+ (tp+fn);
        }
        double   recallMicro=numerator/denominator;

        //Fscore-Micro (Relations between data’s positive labels and those given by a classifier based on sums of per-text decisions)
        double beta=1;
        numerator=(Math.pow(beta,2)+1)*precisionMicro*recallMicro;
        denominator=Math.pow(beta,2)*precisionMicro+recallMicro;
        double fscoreMicro=numerator/denominator;

        //Precision-Macro (An average per-class agreement of the data class labels with those of a classifiers)
        double precisionMacro=0.0;
        for (int i=0;i<numClasses;i++){
            fn=per[i][0];
            fp=per[i][1];
            tp=per[i][2];
            tn=per[i][3];
            precisionMacro=precisionMacro+(tp/(tp+fp));
        }
        precisionMacro=precisionMacro/numClasses;

        //Recall-Micro (An average per-class effectiveness of a classifier to identify class labels)
        double recallMacro=0.0;

        for (int i=0;i<numClasses;i++){
            fn=per[i][0];
            fp=per[i][1];
            tp=per[i][2];
            tn=per[i][3];
            recallMacro=recallMacro+(tp/(tp+fn));
        }
        recallMacro=recallMacro/numClasses;

        //Fscore-Macro (Relations between data’s positive labels and those given by a classifier based on a per-class average)
        beta=1;
        numerator=(Math.pow(beta,2)+1)*precisionMacro*recallMacro;
        denominator=Math.pow(beta,2)*precisionMacro+recallMacro;
        double  fscoreMacro=numerator/denominator;

        setAvgAccuray(confusion.round(avgAccuracy,4));
        setErrRate(confusion.round(errRate,4));
        setPrecisionMicro(confusion.round(precisionMicro,4));
        setRecallMicro(confusion.round(recallMicro,4));
        setFscoreMicro(confusion.round(fscoreMicro,4));
        setPrecisionMacro(confusion.round(precisionMacro,4));
        setRecallMacro(confusion.round(recallMacro,4));
        setFscoreMacro(confusion.round(fscoreMacro,4));
        return;
    }

    public double getAvgAccuray() {
        return avgAccuray;
    }

    public void setAvgAccuray(double avgAccuray) {
        this.avgAccuray = avgAccuray;
    }

    public double getErrRate() {
        return errRate;
    }

    public void setErrRate(double errRate) {
        this.errRate = errRate;
    }

    public double getPrecisionMicro() {
        return precisionMicro;
    }

    public void setPrecisionMicro(double precisionMicro) {
        this.precisionMicro = precisionMicro;
    }

    public double getRecallMicro() {
        return recallMicro;
    }

    public void setRecallMicro(double recallMicro) {
        this.recallMicro = recallMicro;
    }

    public double getFscoreMicro() {
        return fscoreMicro;
    }

    public void setFscoreMicro(double fscoreMicro) {
        this.fscoreMicro = fscoreMicro;
    }

    public double getPrecisionMacro() {
        return precisionMacro;
    }

    public void setPrecisionMacro(double precisionMacro) {
        this.precisionMacro = precisionMacro;
    }

    public double getRecallMacro() {
        return recallMacro;
    }

    public void setRecallMacro(double recallMacro) {
        this.recallMacro = recallMacro;
    }

    public double getFscoreMacro() {
        return fscoreMacro;
    }

    public void setFscoreMacro(double fscoreMacro) {
        this.fscoreMacro = fscoreMacro;
    }

    public void print(){
        System.out.println("\nAccuracy Evaluation Results");
        System.out.println("=======================================");
        System.out.println("\tAverage Accuracy(%)       : " + getAvgAccuray() * 100);
        System.out.println("\tError(%)                  : " + getErrRate() * 100);
        System.out.println("\tPrecision (Micro)(%)      : " + getPrecisionMicro() * 100);
        System.out.println("\tRecall (Micro)(%)         : " + getRecallMicro() * 100);
        System.out.println("\tFscore (Micro)(%)         : " + getFscoreMicro() * 100);
        System.out.println("\tPrecision (Macro)(%)      : " + getPrecisionMacro() * 100);
        System.out.println("\tRecall (Macro)(%)         : " + getRecallMacro() * 100);
        System.out.println("\tFscore (Macro)(%)         : " + getFscoreMacro() * 100);
    }
}
