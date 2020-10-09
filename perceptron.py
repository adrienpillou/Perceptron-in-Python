# Author : Adrien Pillou
# Created : 10/09/2020

# Perceptron library made in Python.

import numpy as np
from model import Model
np.random.seed(0)

class Perceptron:
    def __init__(self, inputs):
        self.inputs = inputs
        self.weights = .01 * np.random.randn(len(self.inputs))
        self.output = 0
        self.sum = 0
        self.error = 0
        self.learning_constant = 1
        self.accuracy = 1.0
        pass
    
    def Forward(self, answer):
        self.Calculate()
        self.Activate()
        self.Validate(answer)

    def Estimate(self):
        self.Calculate()
        self.Activate()
        return self.output

    def Calculate(self):
        self.sum = 0
        for i in range(len(self.inputs)):
            self.sum += self.inputs[i]*self.weights[i]

    def Activate(self):
        if(self.sum>0):
            self.output = 1
        else:
            self.output = -1
    
    def Introduce(self):
        print("This perceptron instance got "+ str(len(self.inputs)) +" inputs.")

    def Validate(self, answer):
        self.error = answer - self.output
        for i in range(len(self.inputs)):
            self.weights[i] += self.learning_constant * self.inputs[i] * self.error

    def Train(self, answer):
        print("Model is now training...")
        self.Forward(answer)
        print("Error = "+str(self.error))
        while(self.error!=0):
            self.Forward(answer)
            print("Error = " + str(self.error)+"\nWeights = "+str(self.weights))
        print("Training complete.\nOutput = " + str(self.output))
        model = Model(self.weights, 'model.json')
        model.save()

    def LoadModel(self):
        model = Model( self.weights, 'model.json')
        model.load()
        if(len(model.weights)!=len(self.inputs)):
            
            print('Weights length is different from inputs length !')
            return
        self.weights = model.weights

    def GetModel(self):
        return self.weights
    
    def SetInputs(self, inputs):
        self.inputs = inputs

    def SetLearningConstant(self, value):
        self.learning_constant = value

    def GetAccuracy(self):
        return self.accuracy

    