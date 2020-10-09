# Author : Adrien Pillou
# Created : 10/09/2020

# This class is used to generate a group of dots needed for testing and training a perceptron.

import matplotlib.pyplot as plt
import numpy as np
from perceptron import Perceptron
import random
from function import Function

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Dataset:
    def __init__(self, size):
        self.size = size
        self.dots = []
        self.create()
    
    def create(self):
        for n in range(0, self.size):
            self.dots.append(Dot(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)))

