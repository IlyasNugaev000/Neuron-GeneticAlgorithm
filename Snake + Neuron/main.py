from Snake.Snake import gameLoop
from Neuron import *

def start():
    population = 100
    number_of_poulation = 0
    neurons = [neuralNetwork(input_nodes, hidden_nodes, hhidden_nodes, output_nodes) for i in range(population)]
    res = gameLoop(neurons, 0, population - 1, number_of_poulation)
    while True:
        res = gameLoop(res[0], res[1], res[2], res[3])


if __name__ == "__main__":
    start()