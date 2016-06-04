# Accuracy evaluation 
A java implementation for calculating the accuracy metrics (Accuracy, Error Rate, Precision(micro/macro), Recall(micro/macro), Fscore(micro/macro)) for 
 classification tasks based on the paper [A systematic analysis of performance measures for classification tasks]
 (http://www.sciencedirect.com/science/article/pii/S0306457309000259) and MATLAB confusion implementation.

# Uses

```java
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
```

# Output

Confusion Results

  	Confusion value
  		c = 0.17
  	Confusion Matrix
  		1 0 1 
  		0 2 0 
  		0 0 2 
  	Indices
  		[1]		[]		[0]
  		[]		[2,3]		[]
  		[]		[]		[4,5]
  	Percentages
  		0.2 0.0 1.0 0.8 
  		0.0 0.0 1.0 1.0 
  		0.0 0.33 0.67 1.0 
  
  
Accuracy Evaluation Results
  
  	Average Accuracy(%)       : 91.11
  	Error(%)                  : 8.89
  	Precision (Micro)(%)      : 88.89
  	Recall (Micro)(%)         : 93.02
  	Fscore (Micro)(%)         : 90.91
  	Precision (Macro)(%)      : 88.89
  	Recall (Macro)(%)         : 94.44
  	Fscore (Macro)(%)         : 91.58


# Note

For C++ Implementation, visit [accuracy-evaluation-cpp](https://github.com/ashokpant/accuracy-evaluation-cpp.git)

For MATLAB Implementation, visit [accuracy-evaluation-matlab](https://github.com/ashokpant/accuracy-evaluation-matlab.git)
