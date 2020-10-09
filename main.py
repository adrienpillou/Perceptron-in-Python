# Author : Adrien Pillou
# Created : 10/09/2020

# Just a file for messing around & test the perceptron. 

import matplotlib.pyplot as plt
import numpy as np
from perceptron import Perceptron
import random
from function import Function
from dataset import Dataset

sampleCount = 12 # Sample count needed for training purposes
dotsCount = 512 # Size of the dataset
bias = 1

# Creating dataset of n dots
dataset = Dataset(dotsCount)

# Adding the Perceptron
perceptron = Perceptron([0, 0, bias])
perceptron.LoadModel()

# Creating & drawing the separation line
line = Function(5, .33)
x = np.linspace(-1, 1, 100)
y1 = line.a*x+line.b
plt.plot(x, y1, 'black')

# Training with randomly picked dots in the dataset
for i in range(sampleCount):
    print("\nStarting training n°"+str(i+1)+"...")
    index = random.randint(0, len(dataset.dots))
    sampleDot = dataset.dots[index-1]
    perceptron.SetInputs([sampleDot.x, sampleDot.y, bias])
    answer = 0
    if(sampleDot.y > line.f(sampleDot.x) ):
        answer = 1
    else:
        answer = -1
    perceptron.Train(answer)

# Estimating each dots from the set
goodGuessCount = 0
for dot in dataset.dots:
    perceptron.SetInputs([dot.x, dot.y, bias])
    if(dot.y>line.f(dot.x)):
        answer = 1
    else: 
        answer = -1
    guess = perceptron.Estimate()
    if(guess == answer):
        goodGuessCount+=1
    color = ''
    if(guess == 1 ):
        color = 'ro'
    else:
        color = 'bo'
    plt.plot(dot.x, dot.y, color)
    perceptron.accuracy = goodGuessCount/len(dataset.dots)

print("Loss = "+"{:.2f}".format(1-perceptron.GetAccuracy()))

# Drawing an estimated separation line from the model weights
w0 = perceptron.weights[0]
w1 = perceptron.weights[1]
w2 = perceptron.weights[2]
a = -(w0/w1)
b = -(w2/w1)
guessed_line = Function(a, b)
y2 = guessed_line.a*x + guessed_line.b
plt.plot(x, y2, 'g--') # Green dashes

# Showing the plot
plt.axis([-1, 1, -1, 1])
plt.ylabel('Perceptron Example')
plt.show()