package com.deepsenselab.accuracy_evaluation;

/**
 * Created by Ashok K. Pant (ashokpant87@gmail.com) on 3/17/16.
 */
public class AccuracyEvaluationExample {
    public static void main(String[] args) {
        // targets: SxQ (S:Classes; Q:Samples)
        // outputs: SxQ (S:Classes; Q:Samples)

        double[][] targets = {
                {1, 1, 0, 0, 0, 0},
                {0, 0, 1, 1, 0, 0},
                {0, 0, 0, 0, 1, 1}
        };
        double[][] outputs = {
                {0.1, 0.86, 0.2, 0.1, .02, 0.1},
                {0.4, 0.12, 0.768, 0.145, 0.1, 0.8},
                {0.454, 0.35, 0.21, 0.0, 0.89, 0.9999}
        };

        Confusion confusion = new Confusion(targets, outputs);
        confusion.print();

        Evaluation evaluation = new Evaluation(confusion);
        evaluation.print();
    }
}
