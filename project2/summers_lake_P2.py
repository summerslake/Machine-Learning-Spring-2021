"""
Lake Summers
Clemson Username: lakes
CPSC 6430
2/8/21
Project 2 Estimator File
"""

#Prompt User
print("Please enter year you'd like to estimate")
year = float(input())

#Use weights computed using model analysis and W100MTimes.txt
estimate = 1.31307195e+01 + (-4.32482706e-02 * year) + (2.06369039e-04 * year * year)

#Print estimated time
print("Estimated time: " + str(estimate))
