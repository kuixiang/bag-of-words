# %% Accuracy Evaluation Example
import evaluate
targets = [[1, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 1]]
outputs = [[0.1, 0.86, 0.2, 0.1, .02, 0.1],
[0.4, 0.12, 0.768, 0.145, 0.1, 0.8],
[0.454, 0.35, 0.21, 0.0, 0.89, 0.9999]]

eval = evaluate.evaluation(targets,outputs)

print('%s\n','Confusion Results')
print('\tConfusion value = %0.2f\n', eval.confusion.c)

print('%s\n','Confusion Matrix')

for row in eval.confusion.cm:
    print('\t')
    for col in row:
        print('%0.2f ', col)

print('\n')
print('%s\n','Indices')
for row in eval.confusion.ind:
    for col in row:
        s=col
        if s == 0:
            print('\t[]')
        else:
            if (s == 1):
                print('\t[%d]',col)
            else:
                print('\t[')

        for ind in s:
            print('%d,', ind)
            print('%d] ',s)
            print('\n')
print('%s\n','Percentages')

for rown in eval.confusion.per:
    print('\t')
    for col in row:
        print('%0.2f ', col)
    print('\n')

print('%s\n','Accuracy Evaluation Results')
print('Average System Accuracy(%%)   : %0.2f\n', eval.avgAccuracy)
print('System Error(%%)              : %0.2f\n', eval.errRate)
print('Precision (Micro)(%%)         : %0.2f\n', eval.precisionMicro)
print('tRecall (Micro)(%%)            : %0.2f\n', eval.recallMicro)
print('Fscore (Micro)(%%)            : %0.2f\n', eval.fscoreMicro)
print('Precision (Macro)(%%)         : %0.2f\n', eval.precisionMacro)
print('Recall (Macro)(%%)            : %0.2f\n', eval.recallMacro)
print('Fscore (Macro)(%%)            : %0.2f\n', eval.fscoreMacro)
