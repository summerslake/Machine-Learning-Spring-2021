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
            X[lineCount,i] = float(lineData[i])
        
      #Increment line count
      lineCount += 1
      #Break if you've reached the number of lines of data specified on the first line of the file
      if(lineCount == numLines):
        break

  file.close()
  return numLines,numFeatures,X

def getCentroids(nameOfFile):
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
        numCentroids = int(lineData[0])

        #Create the centroid matrix
        centroidCoord = np.zeros((numCentroids,2))
      #If not the first line
      else:
        #Populate Matrix

        #Fill in x_1...x_numFeatures
        for i in range(0,2):
            centroidCoord[lineCount,i] = float(lineData[i])
        
      #Increment line count
      lineCount += 1
      #Break if you've reached the number of lines of data specified on the first line of the file
      if(lineCount == numCentroids):
        break

  file.close()
  return numCentroids,centroidCoord

def kMeans(numLines,numCentroids,centroidCoord,X):
    #initialize final Centroid Coords
    finalCentroidCoord = centroidCoord
    
    #initialize pointsChanged
    pointChanged = True

    #initialize clusters
    cluster1 = []
    cluster2 = []

    #Keep track of iterations
    iteration = 0
    #While any cluster assignments change
    while(pointChanged):
        #Set pointChanged to false if not initializing clusters
        if (iteration != 0):
            pointChanged = False
        #For all points
        for i in range(0,numLines):
            # print("Checking point: (" + str(X[i,0]) + "," + str(X[i,1]) + ")")
            #Get distance to Centroid 1
            c1Dist = math.sqrt( (X[i,0]-finalCentroidCoord[0,0])**2 + (X[i,1]-finalCentroidCoord[0,1])**2 )
            #Get distance to Centroid 2
            c2Dist = math.sqrt( (X[i,0]-finalCentroidCoord[1,0])**2 + (X[i,1]-finalCentroidCoord[1,1])**2 )

            #If closer to c1
            if(c1Dist<c2Dist):
                #if point not in cluster 1
                if([X[i,0],X[i,1]] not in cluster1):
                    #Assign point to cluster 1
                    cluster1.append([X[i,0],X[i,1]])

                    #if point in cluster 2, remove it
                    if([X[i,0],X[i,1]] in cluster2):
                        cluster2.remove([X[i,0],X[i,1]])
                        pointChanged = True
    
            #If closer to c2
            else:
                #if point not in cluster 2
                if([X[i,0],X[i,1]] not in cluster2):
                    #Assign point to cluster 2
                    cluster2.append([X[i,0],X[i,1]])
                    
                    #if point in cluster 1, remove it
                    if([X[i,0],X[i,1]] in cluster1):
                        cluster1.remove([X[i,0],X[i,1]])
                        pointChanged = True
        
        #Update Centroids
        #initialize average counters
        cluster1AverageX = 0
        cluster1AverageY = 0
        pointCount = 0
        #Calc Averages
        for point in cluster1:
            cluster1AverageX += point[0]
            cluster1AverageY += point[1]
            pointCount += 1
        cluster1AverageX /= pointCount
        cluster1AverageY /= pointCount

        #initialize average counters
        cluster2AverageX = 0
        cluster2AverageY = 0
        pointCount = 0
        #Calc Averages
        for point in cluster2:
            cluster2AverageX += point[0]
            cluster2AverageY += point[1]
            pointCount += 1
        cluster2AverageX /= pointCount
        cluster2AverageY /= pointCount

        #Update Centroids
        finalCentroidCoord[0,0] = cluster1AverageX
        finalCentroidCoord[0,1] = cluster1AverageY
        finalCentroidCoord[1,0] = cluster2AverageX
        finalCentroidCoord[1,1] = cluster2AverageY
        
        #add iteration count
        iteration += 1
    
    # print("Number of iterations: " + str(iteration))


    return cluster1, cluster2, finalCentroidCoord


# print("Enter the name of your data file: ")
# fileName = input()

(numLines,numFeatures,X) = getData("P5Data.txt")

# print("Enter the name of your centroid file: ")
# fileName = input()

(numCentroids,centroidCoord) = getCentroids("P5Centroids.txt")

# Initial Plot
print("Centroid Coordinates:")
print(centroidCoord)

#Plot x and y data
plot.scatter(X[:,0], X[:,1], color = "purple", marker = "o", label = "Data")
plot.scatter(centroidCoord[0,0],centroidCoord[0,1],color = "red", marker = "v", label = "Centroid 1")
plot.scatter(centroidCoord[1,0],centroidCoord[1,1],color = "green", marker = "v", label = "Centroid 2")
#Start Title
title = "Initial Data Points"
yLabel = "x2 Axis"
xLabel = "x1 Axis"

#Label plot
plot.xlabel(xLabel)
plot.ylabel(yLabel)
plot.title(title)
#Make legend
plot.legend()
#Show the plot
plot.show()

#Run K-means
(cluster1,cluster2,finalCentroidCoord) = kMeans(numLines,numCentroids,centroidCoord,X)

#Plot cluster 1
for x in cluster1:
    plot.scatter(x[0], x[1], color = "red", marker = "o", label = "Data")
#Plot cluster 2
for x in cluster2:
    plot.scatter(x[0], x[1], color = "green", marker = "o", label = "Data")

#Plot final centroids
plot.scatter(finalCentroidCoord[0,0],finalCentroidCoord[0,1],color = "red", marker = "v", label = "Centroid 1")
plot.scatter(finalCentroidCoord[1,0],finalCentroidCoord[1,1],color = "green", marker = "v", label = "Centroid 2")
#Start Title
title = "Clustered Data Points"
yLabel = "x2 Axis"
xLabel = "x1 Axis"

#Label plot
plot.xlabel(xLabel)
plot.ylabel(yLabel)
plot.title(title)
#Show the plot
plot.show()

#Print final centroid coordinates
print("\nFinal centroids are:")
print(finalCentroidCoord)

#Computer overall error
j = 0
numPoints = 0
#add all distances from cluster 1 points to centroid 1
for c1Point in cluster1:
    j += (c1Point[0]-finalCentroidCoord[0,0])**2 + (c1Point[1]-finalCentroidCoord[0,1])**2
    numPoints += 1
#add all distances from cluster 2 points to centroid 2
for c2Point in cluster2:
    j += (c2Point[0]-finalCentroidCoord[1,0])**2 + (c2Point[1]-finalCentroidCoord[1,1])**2
    numPoints +=1
#divide by total number of points
j /= numPoints

#Print overall error
print("Error is " + str(j))


