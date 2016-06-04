

data={'Dog': ['Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Cat', 'Rabbit', 'Cat'],
      'Rabbit': ['Dog', 'Cat', 'Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Rabbit'],
      'Cat': ['Rabbit', 'Dog', 'Cat', 'Cat', 'Rabbit', 'Dog', 'Cat', 'Cat', 'Dog', 'Cat']}

#Contract:
#list list->dictionary
#Purpose: HowMany function takes two lists and counts same elements in two lists and returns a dictionary
#Examples:
#['Dog','Rabbit','Cat'],['Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Cat', 'Rabbit', 'Cat']->
#{'Dog':1,"Rabbit":5,"Cat":4}
def HowMany(lon1,lon2):
    #creates a new dictionary to assign counted items
    new={}
    for i in lon1:
        count=0
        for j in lon2:
            #if first element in lon1 equals first element in lon2 increase count by 1
            if(i==j):
                count+=1
                #add first element of lon1 into dictionary as key and add count value into dictionary as value of the key
        new[i]=count
    return new

print HowMany(['Dog','Rabbit','Cat'],['Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Cat', 'Rabbit', 'Cat'])
print "*********************************************************"


#Contract:
#dictionary->list
#Purpose: takes a dictionary which has lists as values, and calls HowMany function, add output comes from HowMany to new list
#Examples:
#{'Dog': ['Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Cat', 'Rabbit', 'Cat'],
#'Rabbit': ['Dog', 'Cat', 'Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Rabbit'],
#'Cat': ['Rabbit', 'Dog', 'Cat', 'Cat', 'Rabbit', 'Dog', 'Cat', 'Cat', 'Dog', 'Cat']} ->
#[{'Dog': 1, 'Rabbit': 5, 'Cat': 4}, {'Dog': 2, 'Rabbit': 5, 'Cat': 3}, {'Dog': 3, 'Rabbit': 2, 'Cat': 5}]
def DictionaryToList(D):
    dictkeys=D.keys()
    dictvalues=D.values()
    l=[]
    for i in dictvalues:
        l.append(HowMany(dictkeys,i))
    return l

print DictionaryToList(data)
print "*********************************************************"

#Contract:
#dictionary->dictionary
#Examples:
#{'Dog': ['Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Cat', 'Rabbit', 'Cat'],
#'Rabbit': ['Dog', 'Cat', 'Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Rabbit'],
#'Cat': ['Rabbit', 'Dog', 'Cat', 'Cat', 'Rabbit', 'Dog', 'Cat', 'Cat', 'Dog', 'Cat']}->
#{'Dog': {'Dog': 1, 'Rabbit': 5, 'Cat': 4}, 'Rabbit': {'Dog': 2, 'Rabbit': 5, 'Cat': 3}, 'Cat': {'Dog': 3, 'Rabbit': 2, 'Cat': 5}}
def ConfusionMatrix(D):
    lst=DictionaryToList(D)
    lst2=D.keys()
    dictionary=dict(zip(lst2,lst))
    return dictionary

print ConfusionMatrix(data)
print "*********************************************************"

#Contract:
#Dictionary->number
#Puporse: it calculates the accuracy
#Examples:#{'Dog': ['Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Cat', 'Rabbit', 'Cat'],
#'Rabbit': ['Dog', 'Cat', 'Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Rabbit'],
#'Cat': ['Rabbit', 'Dog', 'Cat', 'Cat', 'Rabbit', 'Dog', 'Cat', 'Cat', 'Dog', 'Cat']}-> 0.366666666667
def accuracy(D):
    total=len(D.keys())*len(D.values()[0])
    newdictionary = ConfusionMatrix(D)
    count=0
    for k,v in newdictionary.iteritems():
        for kk,vv in v.iteritems():
            if(k==kk):
                count=count+int(vv)
    return float(count) / (total)

print accuracy(data)






