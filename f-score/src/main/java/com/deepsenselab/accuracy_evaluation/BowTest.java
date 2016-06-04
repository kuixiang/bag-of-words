package com.deepsenselab.accuracy_evaluation;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by xiangkui on 16/6/3.
 */
public class BowTest {
    public static void main(String[] args) {
        String file_target=args[0];
        String file_output=args[1];
        BufferedReader rd_target=null;
        BufferedReader rd_output=null;
        try{
            rd_target = new BufferedReader(new FileReader(file_target));
            rd_output = new BufferedReader(new FileReader(file_output));
            String line_target=null,line_output=null;
            List<List<Double>> targetsList = new ArrayList<List<Double>>();
            List<List<Double>> outputsList = new ArrayList<List<Double>>();
            while(null!=(line_target = rd_target.readLine())){
                String[] cols = line_target.split("\t");
                List<Double> tmpList = new ArrayList<Double>();
                for (String col : cols) {
                    tmpList.add(Double.parseDouble(col));
                }
                targetsList.add(tmpList);
            }
            while(null!=(line_output = rd_output.readLine())){
                String[] cols = line_output.split(",");
                List<Double> tmpList = new ArrayList<Double>();
                for (String col : cols) {
                    tmpList.add(Double.parseDouble(col));
                }
                outputsList.add(tmpList);
            }
            // list to array
            int rows = targetsList.size();
            int cols = targetsList.get(0).size();
            double[][] targets = new double[rows][cols];
            double[][] outputs = new double[rows][cols];

            for(int i=0;i < rows;i++){
                for(int j=0;j <cols;j++){
                    targets[i][j] = targetsList.get(i).get(j);
                    outputs[i][j] = outputsList.get(i).get(j);
                }
            }

            Confusion confusion = new Confusion(targets, outputs);
            confusion.print();

            Evaluation evaluation = new Evaluation(confusion);
            evaluation.print();

        }catch (Exception e){
            e.printStackTrace();
        } finally {
            if(null!=rd_target){
                try {
                    rd_target.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if(null!=rd_output){
                try {
                    rd_output.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }




    }
}
