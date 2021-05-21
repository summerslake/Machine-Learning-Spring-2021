"""
Lake Summers
Clemson Username: lakes
CPSC 6430
2/8/21
Project 2 Quadratic Analysis
"""
import numpy as np
import math

def kNN(trainPointArray,testPointArray):
  #Make counters for test knn results
  fp = 0
  fn = 0
  tp = 0
  tn = 0
  totalErrorCount = 0

  #For all points in testing
  for [xTest,yTest,classificationTest] in testPoints:
    distanceTupleList = []
    #For all points in training
    for [xTrain,yTrain,classificationTrain] in trainPoints:
      #Calc distance from test point to training point
      distance = math.sqrt( ((xTest-xTrain)**2) + ((yTest-yTrain)**2) )
      #Keep track of all dist calculated
      distanceTupleList.append([xTrain,yTrain,classificationTrain,distance])

    # print("Before sort:")
    # print(distanceTupleList)
    #Sort points by distance
    distanceTupleList.sort(key = lambda x: x[3])
    # print("After sort:")
    # print(distanceTupleList)

    #Look at top k points classifications and make guess
    k=3
    #Set classification count
    classificationCount = 0

    #Go through top k points
    for i in range(k):
      #Keep track of classification
      classificationCount += distanceTupleList[i][2]

    #If majority passed
    if classificationCount >= k/2:
      classGuess = 1
    #If majority did not pass
    else:
      classGuess = 0

    #Check if correct in test array
    if (classGuess == classificationTest) and classGuess == 1:
      tp += 1
    elif (classGuess == classificationTest) and classGuess == 0:
      tn += 1
    elif (classGuess != classificationTest) and classGuess == 1:
      # print("False positive error:")
      # print("Test Point: (" + str(xTest) + "," + str(yTest) + ")")
      # print(str(k) + "closest points: ")
      # for i in range(k):
      #   print("(" + str(distanceTupleList[i][0]) + "," + str(distanceTupleList[i][1]) + ") " + "Class: " + str(distanceTupleList[i][2]))
      # print("")
      fp += 1
    elif (classGuess != classificationTest) and classGuess == 0:
      # print("False Negative error:")
      # print("Test Point: (" + str(xTest) + "," + str(yTest) + ")")
      # print(str(k) + "closest points: ")
      # for i in range(k):
      #   print("(" + str(distanceTupleList[i][0]) + "," + str(distanceTupleList[i][1]) + ")" + "Class: " + str(distanceTupleList[i][2]))
      # print("")
      fn += 1

  totalErrorCount = fp+fn
  #Report errors
  return [tp,tn,fp,fn,totalErrorCount]

def getData(nameOfFile):
  file = open(nameOfFile, "r")

  #Set line count to -1
  lineCount = -1
  #For each line in the file
  for line in file:
      #Split by tab
      lineData = line.split("\t")

      #If the first line, get the matrix size info
      if (lineCount == -1):
        #Get size info
        numLines = int(lineData[0])
        numFeatures = int(lineData[1])

        #Create the matrix
        points = np.zeros((numLines,numFeatures+1))
      
      #If not the first line
      else:
        #Populate Matrices

        #Fill in points
        for i in range(0,numFeatures+1):
          points[lineCount,i] = float(lineData[i])
        
      #Increment line count
      lineCount += 1
      #Break if you've reached the number of lines of data specified on the first line of the file
      if(lineCount == numLines):
        break
        
  # print("X is: ")
  # print(X)

  file.close()
  return points

print("Enter the name of your training file: ")
fileName = input()

#Get Training Data
trainPoints = getData(fileName)
# print(testPoints)

print("Enter the name of your testing file: ")
testFileName = input()

#Get Testing Data
testPoints = getData(testFileName)

[tp,tn,fp,fn,totalErrorCount] = kNN(trainPoints,testPoints)
print("False Positive: " + str(fp))
print("False Negative: " + str(fn))
print("True Positive: " + str(tp))
print("True Negative: " + str(tn))

print("Total error: " +  str(totalErrorCount))

accuracy = (tp+tn)/(tp+tn+fp+fn)
print("Accuracy: " + str(accuracy))
precision = tp/(tp+fp)
print("Precision: " + str(accuracy))
recall = tp/(tp+fn)
print("Recall: " + str(recall))
f1 = 2*(1/((1/precision)+(1/recall)))
print("F1: " + str(f1))


