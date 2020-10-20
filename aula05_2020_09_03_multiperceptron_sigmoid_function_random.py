# -*- coding: utf-8 -*-
"""aula05_2020_09_03_multiperceptron_sigmoid_function_random.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Buozu5j5KbsyQDOsoX6164cqit953oQF
"""
import numpy as np
import math
import time

"""## MULTIPERCEPTRON AND SIGMOID FUNCTION RANDOM"""


def sigmoid(value):
    return 1 / (1 + np.exp(-value))


def derived_sigmoid(sig):
    return sig * (1 - sig)


inputs = np.array([[0, 0], 
                   [0, 1], 
                   [1, 0], 
                   [1, 1]])

output_ = np.array([[0],
                    [1],
                    [1],
                    [0]])

weight1 = 2*np.random.random((2,3)) - 1
weight2 = 2*np.random.random((3,1)) - 1

epoch = 10
learning_rate = 0.7
moment = 1.005

for j in range(epoch):
    input_layer = inputs
    sum_synapse1 = np.dot(input_layer, weight1)
    hidden_layer = sigmoid(sum_synapse1)

    sum_synapse2 = np.dot(hidden_layer, weight2)
    output_layer = sigmoid(sum_synapse2)

    output_layer_error = output_ - output_layer
    absolute_average = np.mean(np.abs(output_layer_error))
    print("Error: " + str(absolute_average))

    derivative_output = derived_sigmoid(output_layer)
    delta_output = output_layer_error * derivative_output

    weight2_transposed = weight2.T
    delta_outputx_weight = delta_output.dot(weight2_transposed)
    delta_hidden_layer = delta_outputx_weight * derived_sigmoid(hidden_layer)

    hidden_layer_transposed = hidden_layer.T
    new_weights2 = hidden_layer_transposed.dot(delta_output)
    weight2 = (weight2 * moment) + (new_weights2 * learning_rate)

    transposed_entry_layer = input_layer.T
    new_weights1 = transposed_entry_layer.dot(delta_hidden_layer)
    weight1 = (weight1 * moment) + (new_weights1 * learning_rate)


# OUTPUT
# Error: 0.5001204158164341
# Error: 0.5001405195380415
# Error: 0.5001506241088196
# Error: 0.5001544495503312
# Error: 0.5001546931967644
# Error: 0.5001531551819314
# Error: 0.5001509494614835
# Error: 0.5001487129123772
# Error: 0.5001467743541796
# Error: 0.5001452761393818