"""
Lake Summers
Clemson Username: lakes
CPSC 6430
1/25/21
"""
import matplotlib.pyplot as plot

print("Enter the name of your file: ")
fileName = input()
file = open(fileName, "r")

setosaData = []
versicolorData = []
virginicaData = []

#Make 2D arrays to fill with features
for i in range(4):
    setosaData.append([])
    versicolorData.append([])
    virginicaData.append([])


#For each line in the file
for line in file:
    #Split by tab
    lineData = line.split("\t")

    #If not the first line
    if (len(lineData) != 2):
        #Add Setosa Data
        if (lineData[4] == 'setosa\n'):
            setosaData[0].append(float(lineData[0]))
            setosaData[1].append(float(lineData[1]))
            setosaData[2].append(float(lineData[2]))
            setosaData[3].append(float(lineData[3]))
        #Add Versicolor Data
        elif (lineData[4] == 'versicolor\n'):
            versicolorData[0].append(float(lineData[0]))
            versicolorData[1].append(float(lineData[1]))
            versicolorData[2].append(float(lineData[2]))
            versicolorData[3].append(float(lineData[3]))
        #Add Viginica Data
        else:
            virginicaData[0].append(float(lineData[0]))
            virginicaData[1].append(float(lineData[1]))
            virginicaData[2].append(float(lineData[2]))
            virginicaData[3].append(float(lineData[3]))

file.close()

#Prompt user for 2 features
print("You can do a plot of any two features of the Iris Data set")
print("The feature codes are: ")
print("\t0 = sepal length")
print("\t1 = sepal width")
print("\t2 = petal length")
print("\t3 = petal width")

#Loop until user says they don't want another plot
repeatPlot = True
while repeatPlot == True:
    #Get x and y feature
    xFeature = int(input("Enter feature code for the horizontal axis: "))
    yFeature = int(input("Enter feature code for the vertical axis: "))

    #Plot x and y data for each Iris Type
    plot.scatter(setosaData[xFeature], setosaData[yFeature], color = "green", marker = "v", label = "Setosa")
    plot.scatter(versicolorData[xFeature], versicolorData[yFeature], color = "blue", marker = "o", label = "Versicolor")
    plot.scatter(virginicaData[xFeature], virginicaData[yFeature], color = "red", marker = "+", label = "Virginica")
    
    #Start Title
    title = "Iris Flower Plot: "

    #Y Label/Title Creation
    if(yFeature == 0):
        yLabel = "Sepal Length"
        title += "Sepal Length vs "
    elif(yFeature == 1):
        yLabel = "Sepal Width"
        title += "Sepal Width vs "
    elif(yFeature == 2):
        yLabel = "Petal Length"
        title += "Petal Length vs "
    elif(yFeature == 3):
        yLabel = "Petal Width"
        title += "Petal Length vs "

    #X Label/Title Creation
    if(xFeature == 0):
        xLabel = "Sepal Length"
        title += "Sepal Length"
    elif(xFeature == 1):
        xLabel = "Sepal Width"
        title += "Sepal Width"
    elif(xFeature == 2):
        xLabel = "Petal Length"
        title += "Petal Length"
    elif(xFeature == 3):
        xLabel = "Petal Width"
        title += "Petal Width"

    #Label plot
    plot.xlabel(xLabel)
    plot.ylabel(yLabel)
    plot.title(title)
    #Make legend
    plot.legend()
    #Show the plot
    plot.show()
 
    #Ask for repeat
    repeatPlot = input("Would you like to do another plot? (y/n) ")

    #Parse input
    if (repeatPlot == "y"):
        repeatPlot = True
    elif (repeatPlot == "n"):
        repeatPlot = False
