import numpy


class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, hhiddennodes, outputnodes): 
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.hhnodes = hhiddennodes
        self.onodes = outputnodes
        
        
        self.wih = numpy.random.rand(self.hnodes, self.inodes)
        self.whh = numpy.random.rand(self.hhnodes, self.hnodes)
        self.who = numpy.random.rand(self.onodes, self.hhnodes)
        
        # Функция активации
        self.activation_function = lambda x: numpy.maximum(x, 0)
    

    #Создаем функцию , которая будет принимать входные данные
    def query(self, inputs_list):
            inputs = numpy.array(inputs_list, ndmin=2).T
            hidden_inputs = numpy.dot(self.wih, inputs)
            hidden_outputs = self.activation_function(hidden_inputs)
            hhidden_inputs = numpy.dot(self.whh, hidden_outputs)
            hhidden_outputs = self.activation_function(hhidden_inputs)
            final_inputs = numpy.dot(self.who, hhidden_outputs)
            final_outputs = self.activation_function(final_inputs)
            
            return final_outputs

#Подаем конкретное значение для входного , скрытого ,выходного слоев соответственно
input_nodes = 12
hidden_nodes = 10
hhidden_nodes = 8
output_nodes = 4
