"""
Lake Summers
Clemson Username: lakes
CPSC 6430
3/8/21
Project 4 Logistic Regression
"""
import numpy as np
import math
import matplotlib.pyplot as plot

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

        #Create the X matrix
        X = np.zeros((numLines,numFeatures))
      #If not the first line
      else:
        #Populate Matrix

        #Fill in x_1...x_numFeatures
        for i in range(0,numFeatures):
          X[lineCount,i] = float(lineData[i-1])
        
      #Increment line count
      lineCount += 1
      #Break if you've reached the number of lines of data specified on the first line of the file
      if(lineCount == numLines):
        break

  file.close()
  return numLines,numFeatures,X

def gradDesc(numLines,numFeatures,X,y):
  #Set number of iterations
  iterations = 110000
  #Set j to 0s
  j = np.zeros(iterations)
  #Set o1xm for cost calculation
  o1xm = np.ones((1,numLines))
  #Set weights to 0
  w = np.zeros((numFeatures+1,1))
  #Set learning rate
  alpha = 0.01

  print("\nIterations: " + str(iterations))
  #Print initial vals
  print("Initial Values:")
  print("W: ")
  print(w)
  print("Alpha:" + str(alpha) + "\n")

  print("********NOTE: Please close plot of J vs Iterations in order to be prompted for testing file******\n\n")

  #For j iterations
  for i in range(0,iterations):
    # print("Iteration: " + str(j))

    #Get hypothesis guess
    H = 1/(1+math.e**(-1*(np.dot(X,w))))
    # print("Hypothesis results: ")
    # print(H)

    #Get cost result
    cost = -(y * np.log(H)) - (1-y) * np.log(1-H)

    #Update weights
    w = w - np.transpose((alpha/numLines) * np.dot(np.transpose(H-y),X))
    # print("W: ")
    # print(w)

    #Get J
    j[i] = (1/numLines) * np.dot(o1xm,cost)

  print("Final J Value after gradient descent: " + str(j[iterations-1]))
  #Plot x and y data for each Iris Type
  plot.scatter(range(1,iterations+1), j, color = "green", marker = "v", label = "J vs Iteration")
  
  #Start Title
  title = "J Value vs Iteration"
  yLabel = "J Value"
  xLabel = "Number of Iterations"

  #Label plot
  plot.xlabel(xLabel)
  plot.ylabel(yLabel)
  plot.title(title)
  #Make legend
  plot.legend()
  #Show the plot
  plot.show()

  return w

def getPredictions(numLines,numFeatures,X,y,computedWeights):
  #Make counters for prediction results
  fp = 0
  fn = 0
  tp = 0
  tn = 0

  #Set o1xm for cost calculation
  o1xm = np.ones((1,numLines))

  #Get hypothesis results
  H = 1/(1+math.e**(-1*(np.dot(X,computedWeights))))
  # print("Hypothesis results: ")
  # print(H)

  hypoIndex = 0

  for result in H:
    # If prediction is 1
    if result >= 0.5:
      # If actual result is 1
      if y[hypoIndex] == 1:
        #True positive
        tp += 1
      else:
        #False positive
        fp += 1
    else:
      # If actual result is 1
      if y[hypoIndex] == 1:
        #False negative
        fn += 1
      else:
        #True negative
        tn += 1
        
    hypoIndex += 1
      
  #Get cost result
  cost = -(y * np.log(H)) - (1-y) * np.log(1-H)

  #Get J
  j = (1/numLines) * np.dot(o1xm,cost)

  return j,fp,fn,tp,tn




print("Enter the name of your training file: ")
fileName = input()

#Get Training Data
(numLinesTrain,numFeaturesTrain,xTrain,yTrain) = getData(fileName)

#Compute weights
weights = gradDesc(numLinesTrain,numFeaturesTrain,xTrain,yTrain)

# Print computed weights
print("Final computed weights: ")
print(weights)
print("")

print("Enter the name of your testing file: ")
testFileName = input()

# Get Testing Data
(numLinesTest,numFeaturesTest,xTest,yTest) = getData(testFileName)

# Get predictions
j,fp,fn,tp,tn = getPredictions(numLinesTest,numFeaturesTest,xTest,yTest,weights)

print("\nFinal J: " + str(float(j)))

#Make predictions and compare
print("False Positive: " + str(fp))
print("False Negative: " + str(fn))
print("True Positive: " + str(tp))
print("True Negative: " + str(tn))

accuracy = (tp+tn)/(tp+tn+fp+fn)
print("Accuracy: " + str(accuracy))
precision = tp/(tp+fp)
print("Precision: " + str(accuracy))
recall = tp/(tp+fn)
print("Recall: " + str(recall))
f1 = 2*(1/((1/precision)+(1/recall)))
print("F1: " + str(f1))


