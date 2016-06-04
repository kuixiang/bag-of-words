package com.deepsenselab.accuracy_evaluation;

import java.util.Arrays;

/**
 * Created by Ashok K. Pant (ashokpant87@gmail.com) on 3/17/16.
 */
public class Confusion {
    private int classes;
    private double[][] per = new double[classes][4];
    private String[][] ind = new String[classes][classes];
    private int[][] cm = new int[classes][classes];
    private int samples;
    private double c;

    Confusion() {}

    Confusion(int classes, int samples) {
        this.classes = classes;
        this.samples = samples;
    }

    Confusion(double targets[][], double outputs[][]){
        confusion(targets,outputs);
    }

    public void confusion(double targets[][], double outputs[][]) {
            /* confusion takes an SxQ (S:Classes; Q:Samples)target and output matrices
	         T and Y, where each column of T is all zeros with one 1 indicating the target
	         class, and where the columns of Y have values in the range [0,1], the largest
	         Y indicating the models output class.

	        It returns the confusion value C, indicating the fraction of samples
	        misclassified, CM an SxS confusion matrix, where CM(i,j) is the number
	        of target samples of the ith class classified by the outputs as class j.

	        IND is an SxS cell array whose elements IND{i,j} contain the sample
	        indices of class i targets classified as class j.

	        PER is an Sx4 matrix where each ith row summarizes these percentages
	        associated with the ith class:
	            S(i,1) = false negative rate = false negatives / all output negatives
	            S(i,2) = false positive rate = false positives / all output positives
	            S(i,3) = true positive rate = true positives / all output positives
	            S(i,4) = true negative rate = true negatives / all output negatives
	           */

        int numClasses = outputs.length;
        setClasses(numClasses);
        if (numClasses == 1) {
            System.out.println("Number of classes must be greater than 1.");
            return;
        }

        // Unknown/don't-care targets
        //TODO Handle infinite or nan numbers in the target and output.

        int numSamples = targets[0].length;
        setSamples(numSamples);
        //Transform outputs (maximum value is set to 1 and other values to 0, column-wise)
        for (int col = 0; col < numSamples; col++) {
            double max = outputs[0][col];
            int ind = 0;

            for (int row = 1; row < numClasses; row++) {
                if (outputs[row][col] > max) {
                    max = outputs[row][col];
                    ind = row;
                }
                outputs[row][col] = 0.0;
            }
            outputs[0][col] = 0.0;
            outputs[ind][col] = 1;
        }

        // Confusion value
        int count = 0;
        for (int row = 0; row < numClasses; row++) {
            for (int col = 0; col < numSamples; col++) {
                if (targets[row][col] != outputs[row][col])
                    count++;
            }
        }
        double c = (double) count / (double) (2 * numSamples);

        // Confusion matrix
        int[][] cm = new int[numClasses][numClasses];
        for (int row = 0; row < numClasses; row++) {
            for (int col = 0; col < numClasses; col++) {
                cm[row][col] = 0;
            }
        }

        int[] i = new int[numSamples];
        int[] j = new int[numSamples];

        for (int col = 0; col < numSamples; col++) {
            for (int row = 0; row < numClasses; row++) {
                if (targets[row][col] == 1.0) {
                    i[col] = row;
                    break;
                }
            }
        }

        for (int col = 0; col < numSamples; col++) {
            for (int row = 0; row < numClasses; row++) {
                if (outputs[row][col] == 1.0) {
                    j[col] = row;
                    break;
                }
            }
        }

        for (int col = 0; col < numSamples; col++) {
            cm[i[col]][j[col]] = cm[i[col]][j[col]] + 1;
        }

        // Indices
        int[][][] ind1 = new int[numClasses][numClasses][3];

        String[][] ind = new String[numClasses][numClasses];
        for (int row = 0; row < numClasses; row++)
            for (int col = 0; col < numClasses; col++)
                ind[row][col] = "";


        for (int col = 0; col < numSamples; col++) {
            if (ind[i[col]][j[col]].equals(""))
                ind[i[col]][j[col]] = new StringBuilder().append(col).toString();
            else
                ind[i[col]][j[col]] = new StringBuilder().append(ind[i[col]][j[col]]).append(",").append(col).toString();
        }

        // Percentages
        double[][] per = new double[numClasses][4];
        for (int row = 0; row < numClasses; row++) {
            for (int col = 0; col < 4; col++) {
                per[row][col] = 0.0;
            }
        }

        for (int row = 0; row < numClasses; row++) {
            double[] yi = new double[numSamples];
            double[] ti = new double[numSamples];
            for (int col = 0; col < numSamples; col++) {
                yi[col] = outputs[row][col];
                ti[col] = targets[row][col];

            }

            int a = 0, b = 0;
            for (int col = 0; col < numSamples; col++) {
                if (yi[col] != 1 && ti[col] == 1) a = a + 1;
                if (yi[col] != 1) b = b + 1;
            }
            per[row][0] = (double) a / (double) b;


            a = 0;
            b = 0;
            for (int col = 0; col < numSamples; col++) {
                if (yi[col] == 1 && ti[col] != 1) a = a + 1;
                if (yi[col] == 1) b = b + 1;
            }
            per[row][1] = (double) a / (double) b;


            a = 0;
            b = 0;
            for (int col = 0; col < numSamples; col++) {
                if (yi[col] == 1 && ti[col] == 1) a = a + 1;
                if (yi[col] == 1) b = b + 1;
            }
            per[row][2] = (double) a / (double) b;

            a = 0;
            b = 0;
            for (int col = 0; col < numSamples; col++) {
                if (yi[col] != 1 && ti[col] != 1) a = a + 1;
                if (yi[col] != 1) b = b + 1;
            }
            per[row][3] = (double) a / (double) b;

        }

        //NAN handling
        for (int row = 0; row < numClasses; row++) {
            for (int col = 0; col < 4; col++) {
                if (Double.isNaN(per[row][col]))
                    per[row][col] = 0.0;
            }
        }

        setC(round(c, 2));
        setCM(cm);
        setInd(ind);
        setPer(per);
    }

    public double round(double valueToRound, int numberOfDecimalPlaces) {
        double multiplicationFactor = Math.pow(10, numberOfDecimalPlaces);
        double interestedInZeroDPs = valueToRound * multiplicationFactor;
        return Math.round(interestedInZeroDPs) / multiplicationFactor;
    }

    public double getC() {
        return c;
    }

    public void setC(double c) {
        this.c = c;
    }

    public int[][] getCM() {
        return cm;
    }

    public void setCM(int[][] cm) {
        this.cm = cm;
    }

    public String[][] getInd() {
        return ind;
    }

    public void setInd(String[][] ind) {
        this.ind = ind;
    }

    public double[][] getPer() {
        return per;
    }

    public void setPer(double[][] per) {
        this.per = per;
    }

    public int getClasses() {
        return classes;
    }

    public void setClasses(int classes) {
        this.classes = classes;
    }

    public int getSamples() {
        return samples;
    }

    public void setSamples(int samples) {
        this.samples = samples;
    }

    public void printC() {
        System.out.println("\tConfusion value\n\t\tc = " + c);
    }

    public void printCM() {
        System.out.println("\tConfusion Matrix");
        for (int row = 0; row < getClasses(); row++) {
            System.out.print("\t\t");
            for (int col = 0; col < getClasses(); col++) {
                System.out.print(getCM()[row][col]+ " ");
            }
            System.out.println();
        }
    }

    public void printInd() {
        System.out.println("\tIndices");
        for (int row = 0; row < classes; row++) {
            for (int col = 0; col < classes; col++) {
                System.out.print("\t\t[" + ind[row][col] + "]");
            }
            System.out.println();
        }
    }

    public void printPer() {
        System.out.println("\tPercentages");
        for (int row = 0; row < classes; row++) {
            System.out.print("\t\t");
            for (int col = 0; col < 4; col++) {
                System.out.print(round(per[row][col],2)+ " ");
            }
            System.out.println();
        }
    }

    public void print(){
        System.out.println("Confusion Results");
        System.out.println("=======================================");
        printC();
        printCM();
        printInd();
        printPer();
    }
}
