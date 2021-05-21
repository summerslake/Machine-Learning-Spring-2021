"""
Lake Summers
Clemson Username: lakes
CPSC 6430
2/8/21
Project 2 Quadratic Analysis
"""
import numpy as np

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

        #Create the matrices
        X = np.zeros((numLines,numFeatures+2))
        y = np.zeros((numLines,1))
      #If not the first line
      else:
        #Populate Matrices

        #Set x_0 to 1
        X[lineCount,0] = 1

        #Fill in x_1...x_numFeatures
        for i in range(1,numFeatures+1):
          X[lineCount,i] = float(lineData[i-1])
          X[lineCount,i+1] = float(lineData[i-1])*float(lineData[i-1])
        
        #Fill in y
        y[lineCount] = lineData[numFeatures]
        
      #Increment line count
      lineCount += 1
      #Break if you've reached the number of lines of data specified on the first line of the file
      if(lineCount == numLines):
        break
        
  # print("X is: ")
  # print(X)

  file.close()
  return numLines,numFeatures,X,y

def getWeights(X,y):
  #Calc Weights
  A = np.linalg.pinv(np.dot(X.T,X))
  B = np.dot(X.T,y)
  weights = np.dot(A,B)
  return weights

def getJ(numLines,X,w,y):
  #Calc J
  C = np.dot(X,w) - y
  J = (1/numLines)*np.dot(C.T,C)
  return J

print("Enter the name of your training file: ")
fileName = input()

#Get Training Data
(trainLines,trainFeatures,trainX,trainY) = getData(fileName)

#Calc Training Weights
trainW = getWeights(trainX,trainY)
#Print Training Weights
print("\nWeights from training file are: ")
print(trainW)
print("\n")


#Calc Training file J
trainJ = getJ(trainLines,trainX,trainW,trainY)
#Print Training file J
print("J value of training file is: ")
print(trainJ)
print("\n")

print("Enter the name of your testing file: ")
testFileName = input()

#Get Testing Data
(testLines,testFeatures,testX,testY) = getData(testFileName)

#Calc Testing file J
testJ = getJ(testLines,testX,trainW,testY)
#Print Testing file J
print("\nJ value of testing file is: ")
print(testJ)
print("\n")