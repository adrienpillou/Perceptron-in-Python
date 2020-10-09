# Author : Adrien Pillou
# Created : 10/09/2020

# This class is used to save & load perceptron's weights on your system.

import json
import os

class Model:
    def __init__(self, weights, file_name):
        self.weights = weights
        self.file_name = file_name

    # Saving Perceptron model into a json file
    def save(self):
        data = {}
        data['weights'] = []
        for w in self.weights:
            data['weights'].append(w)
        complete_file_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)), self.file_name)
        with open(complete_file_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    # Loading Perceptron model into a json file
    def load(self):
        complete_file_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)), self.file_name)
        if(not os.path.exists(complete_file_path)):
            print("The file '" + self.file_name+ "' does not exists !" )
            return
        with open(os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)), self.file_name)) as json_file:
            data = json.load(json_file)
            self.weights = data['weights']
            return data['weights']
