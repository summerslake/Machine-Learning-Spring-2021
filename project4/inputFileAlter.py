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
        X = np.zeros((numLines,numFeatures+1))
        y = np.zeros((numLines,1))
      #If not the first line
      else:
        #Populate Matrices

        #Set x_0 to 1
        X[lineCount,0] = 1

        #Fill in x_1...x_numFeatures
        for i in range(1,numFeatures+1):
          X[lineCount,i] = float(lineData[i-1])
        
        #Fill in y
        y[lineCount] = float(lineData[numFeatures])
        
      #Increment line count
      lineCount += 1
      #Break if you've reached the number of lines of data specified on the first line of the file
      if(lineCount == numLines):
        break

  file.close()
  return numLines,numFeatures,X,y

numLines,numFeatures,X,y = getData("P3train.txt")

# print("X: ")
# print(X)
# print("X[0,1] is: " + str(X[0][1]))
# print("X[1,1] is: " + str(X[1][1]))
# print("X[2,1] is: " + str(X[2][1]))

# print("Y: ")
# print(y)


file = open("newestP3Train.txt", "w")
file.write(str(numLines)+"\t"+str(24)+"\n")

thePower = 4
totalFeatureCount = 1
for k in range(0,numLines):
    for j in range(thePower+1):
        for i in range(thePower+1):
            if(j == 0 and i == 0):
                #Nothing
                print("Would print 0,0")
            else:
                print("x" + str(totalFeatureCount) + ": x1^" + str(i) + " x2^" + str(j))
                temp = (X[k][1]**i)*(X[k][2]**j)
                file.write(str(temp)+"\t")
                totalFeatureCount += 1
    temp = float(y[k])
    print("\n")
    file.write(str(temp)+"\n")


file.close()


numLines,numFeatures,X,y = getData("P3test.txt")

file = open("newestP3Test.txt", "w")
file.write(str(numLines)+"\t"+str(24)+"\n")

for k in range(0,numLines):
    for j in range(thePower+1):
        for i in range(thePower+1):
            if(j == 0 and i == 0):
                #Nothing
                print("Would print 0,0")
            else:
                print("Writing x1^" + str(i) + " x2^" + str(j))
                temp = (X[k][1]**i)*(X[k][2]**j)
                file.write(str(temp)+"\t")
    temp = float(y[k])
    print("\n")
    file.write(str(temp)+"\n")


file.close()