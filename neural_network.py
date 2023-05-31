import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.layers import Dense, Activation
from tensorflow import keras
from keras.models import Sequential
import numpy as np
from constance import FIELD_SIZE


class NeuralNetwork():
    def __init__(self) -> None:

        self.neuralNet = Sequential()

        # create the dense input layer
        self.neuralNet.add(Dense(6,
                                 input_shape=(6,), activation='selu'))

        # create second layer (first hidden layer)
        self.neuralNet.add(Dense(14, activation='selu'))

        # create third and last layer
        self.neuralNet.add(Dense(4, activation='softmax'))

        self.neuralNet.summary()

    def set_weights(self, weights_list: list[float]):
        weights = self.neuralNet.get_weights()
        current_index = 0
        #  Идёт замена весов (берётся из особей в поколении)
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if isinstance(weights[i][j], np.ndarray):
                    for k in range(len(weights[i][j])):
                        weights[i][j][k] = weights_list[current_index]
                        current_index += 1
                else:
                    weights[i][j] = weights_list[current_index]
                    current_index += 1
        self.neuralNet.set_weights(weights)

    #  Выщитываются коэффициенты
    def predict(self, applex_dist: float,
                appley_dist: float, near_coords: list[float]):
        return self.neuralNet(np.array([np.array([applex_dist, appley_dist, *near_coords])]))#, *snake_xs, *snake_ys])]))
