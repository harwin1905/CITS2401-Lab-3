#Student Name: Harwinddranath Muralitheran
#Student ID: 22254937
#CITS2401 - Lab 3 Part 1

import numpy as np
import math as m
import scipy
import matplotlib.pyplot as plt

#Part 1

def microcar(expected, actual):
    exp_x = []
    exp_y = []
    exp_dist = []
    act_x = []
    act_y = []
    act_dist = []
    #print(expected)
    for i in range(len(expected)):
        total_distance = []
        A = 0
        B = 0
        estimate = np.loadtxt(expected[i], delimiter = ",", dtype = '|S4, i4, i4')
        
        for est in estimate:
            dist = est[1] * est[2]
            if est[0] == b'N':
                B += dist
            elif est[0] == b'S':
                B -= dist
            elif est[0] == b'E':
                A += dist
            elif est[0] == b'W':
                A -= dist
            else:
                pass
        
            total_distance.append(dist)
        exp_x.append(A)
        exp_y.append(B)
        exp_dist.append(sum(total_distance))
    
        
    for i in range(len(actual)):
        total_distance = []
        A = 0
        B = 0
        travelled = np.loadtxt(actual[i], delimiter = ",", dtype = '|S4, i4, i4')
        
        for trav in travelled:
            dist = trav[1] * trav[2]
            if trav[0] == b'N':
                B += dist
            elif trav[0] == b'S':
                B -= dist
            elif trav[0] == b'E':
                A += dist
            elif trav[0] == b'W':
                A -= dist
            else:
                pass
            total_distance.append(dist)
        act_x.append(A)
        act_y.append(B)
        act_dist.append(sum(total_distance))
        
   # print(np.array(exp_x), np.array(exp_y), np.array(exp_dist), np.array(act_x),
           #np.array(act_y), np.array(act_dist))
    
    return(np.array(exp_x), np.array(exp_y),np.array(act_x), np.array(act_y),
           np.array(exp_dist), np.array(act_dist))

microcar(['exp1.csv' ,'exp2.csv'], ['act1.csv' , 'act2.csv'])

#Part 2

def plotmicrocar(expected, actual):
    results = microcar(expected, actual)

    #Bar-Plot 
    expected_distance = results[4]
    actual_distance = results[5]
    bar_width = 0.25
    plt.subplot(2,1,1)
    bar_graph1 = plt.bar(np.arange(len(expected_distance)), expected_distance, bar_width,color='blue', label='Expected_Distance')
    bar_graph2 = plt.bar(np.arange(len(expected_distance)) + bar_width, actual_distance, bar_width, color='black', label='Actual Distance')
    plt.xlabel('mcar')
    plt.ylabel('Dist')
    plt.title('Expected vs Actual Distances')
    plt.xticks(np.arange(len(expected_distance)) + 0.15, range(len(expected_distance)))
    plt.legend()
    
    #Scatter-Plot 1 
    plt.subplot(2,2,3)
    exp_hori = len(results[0])
    for x in range(exp_hori):
        plt.scatter(results[0][x],results[1][x], label=("mivCar "+str(x)))
    axes = plt.gca()
    axes.set_xlim([-60,60])
    axes.set_ylim([-60,60])
    plt.xlabel('x Displacement (Meters)')
    plt.ylabel('y Displacement (Meter)')
    plt.title('E')
    plt.legend()


    #Scatter-Plot 2
    plt.subplot(2,2,4)
    act_hori = len(results[0])
    for x in range(act_hori):
        plt.scatter( results[2][x],results[3][x],marker='x', label=("mivCar "+str(x)))
    axes = plt.gca()
    axes.set_xlim([-60,60])
    axes.set_ylim([-60,60])
    plt.xlabel('x Displacement (Meters)')
    plt.ylabel('y Displacement (Meters)')
    plt.title('A')
    plt.legend()
    plt.show()
    
plotmicrocar(['exp1.csv', 'exp2.csv'], ['act1.csv', 'act2.csv'])