import pygame
import time
import random
import sys
sys.path.insert(0, 'C:/Users/Ильяс/Desktop/Snake + Neuron/Neuron')
sys.path.insert(0, 'C:/Users/Ильяс/Desktop/Snake + Neuron/GenAlgoritm')
import Neuron
import GenAlgoritm
import numpy as np
import copy

 
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 120
dis_height = 120
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')
 
clock = pygame.time.Clock()
fitness_list = []
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def calculate_sensors_information(snake_List: list, food_block: list,
head: list) -> list:
    sensors_information = []
    default_size = 220
    snake_barrier_up = default_size
    snake_barrier_down = default_size
    snake_barrier_left = default_size
    snake_barrier_right = default_size 
    for k in range(len(snake_List) - 1):
        if snake_List[k][0] == head[0]:
            if snake_List[k][1] < head[1] and (head[1] - snake_List[k][1]) < snake_barrier_up:
                snake_barrier_up = head[1] - snake_List[k][1]
            if snake_List[k][1] > head[1] and (snake_List[k][1] - head[1]) < snake_barrier_down:
                snake_barrier_down = snake_List[k][1] - head[1]
        elif snake_List[k][1] == head[1]:
            if snake_List[k][0] < head[0] and(head[0] - snake_List[k][0]) < snake_barrier_left:
                snake_barrier_left = head[0] - snake_List[k][0]
            if snake_List[k][0] > head[0] and (snake_List[k][0] - head[0]) < snake_barrier_right:
                snake_barrier_right = snake_List[k][0] - head[0]
    sensors_information.append(head[1] - food_block[1])
    sensors_information.append(head[0] - food_block[0])
    sensors_information.append(food_block[1] - head[1])
    sensors_information.append(food_block[0] - head[0])
    sensors_information.append(head[0])
    sensors_information.append(head[1])
    sensors_information.append(dis_width - head[0] - snake_block)
    sensors_information.append(dis_height - head[1] - snake_block)
    sensors_information.append(snake_barrier_up - snake_block)
    sensors_information.append(snake_barrier_down - snake_block)
    sensors_information.append(snake_barrier_left - snake_block)
    sensors_information.append(snake_barrier_right - snake_block)
    
    return sensors_information


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop(neurons, current, maximum, number_of_poulation, show=False):
    game_over = False
    game_close = False
    time = 100
    dtime = 100
    fitness_time = 0
 
    x1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    y1 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    x1_change = 105
    y1_change = 105

 
    snake_List = []
    Length_of_snake = 3
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        time -= 1
        fitness_time += 1
        if game_close == True:
            if show == True:
                print(GenAlgoritm.fitness(fitness_time, Length_of_snake - 3))
                return
            cur = current + 1
            global fitness_list
            fitness_list.append(GenAlgoritm.fitness(fitness_time, Length_of_snake - 3))
            if cur == maximum + 1:
                # Конец популяции
                print(number_of_poulation)
                neurons_copy = [copy.deepcopy(neurons[fitness_list.index(max(fitness_list))])]
                cum_sum_list = np.cumsum(fitness_list)
                norm_cum_sum = cum_sum_list / sum(fitness_list)
                print(fitness_list)
                while len(neurons_copy) <= maximum:
                    p1 = GenAlgoritm.roulette(norm_cum_sum)
                    p2 = GenAlgoritm.roulette(norm_cum_sum)
                    neurons_copy.append(copy.deepcopy(neurons[p1]))
                    neurons_copy.append(copy.deepcopy(neurons[p2]))
                    if (random.random() < 0.6):

                        new_res_wih = []
                        new_res_whh = []
                        new_res_who = []
                        new_res_wih.append(list(copy.deepcopy(neurons[p1].wih)))
                        new_res_wih.append(list(copy.deepcopy(neurons[p2].wih)))
                        new_res_whh.append(list(copy.deepcopy(neurons[p1].whh)))
                        new_res_whh.append(list(copy.deepcopy(neurons[p2].whh)))
                        new_res_who.append(list(copy.deepcopy(neurons[p1].who)))
                        new_res_who.append(list(copy.deepcopy(neurons[p2].who)))
                        first_wih = GenAlgoritm.listmerge3(new_res_wih[0])
                        second_wih = GenAlgoritm.listmerge3(new_res_wih[1])
                        first_whh = GenAlgoritm.listmerge3(new_res_whh[0])
                        second_whh = GenAlgoritm.listmerge3(new_res_whh[1])
                        first_who = GenAlgoritm.listmerge3(new_res_who[0])
                        second_who = GenAlgoritm.listmerge3(new_res_who[1])

                        childrens_wih = np.array(GenAlgoritm.mutation(GenAlgoritm.mating(new_res_wih)))
                        childrens_whh = np.array(GenAlgoritm.mutation(GenAlgoritm.mating(new_res_whh)))
                        childrens_who = np.array(GenAlgoritm.mutation(GenAlgoritm.mating(new_res_who)))

                        neurons_copy[-2].wih = childrens_wih[0]
                        neurons_copy[-1].wih = childrens_wih[1]
                        neurons_copy[-2].whh = childrens_whh[0]
                        neurons_copy[-1].whh = childrens_whh[1]
                        neurons_copy[-2].who = childrens_who[0]
                        neurons_copy[-1].who = childrens_who[1]

                cur = 0
                best_neuron = fitness_list.index(max(fitness_list))
                fitness_list = []
                gameLoop(neurons, best_neuron, maximum, number_of_poulation, True)
                return neurons_copy, cur, maximum, number_of_poulation+1
            else:
                return neurons, cur, maximum, number_of_poulation
        dis.fill(blue)
        if show:
            food = pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        res = calculate_sensors_information(snake_List, [foodx, foody], snake_Head)
        if show:
            pass
            #print("Y", res[0])
            #print("X", res[1])
        neuron_answer = neurons[current].query(res).tolist()
        global snake_speed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake_speed += 10
                elif event.key == pygame.K_LEFT:
                    snake_speed -= 10
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if (neuron_answer.index(max(neuron_answer)) == 0) and (x1_change <= 0 or x1_change == 105):
            x1_change = -snake_block
            y1_change = 0
        elif (neuron_answer.index(max(neuron_answer)) == 1) and (x1_change >= 0 or x1_change == 105):
            x1_change = snake_block
            y1_change = 0
        elif (neuron_answer.index(max(neuron_answer)) == 2) and (y1_change <= 0 or x1_change == 105):
            y1_change = -snake_block
            x1_change = 0
        elif (neuron_answer.index(max(neuron_answer)) == 3) and (y1_change >= 0 or x1_change == 105):
            y1_change = snake_block
            x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 or time == 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        if show:
            our_snake(snake_block, snake_List)
            pygame.display.update()
            Your_score(Length_of_snake - 3)

        #res = calculate_sensors_information(snake_List, food, snake_Head)
        #print(neurons[current].query(res))
        #print(calculate_sensors_information(snake_List, food, sensors_information, x1_change, y1_change, snake_Head))
 
        if x1 == foodx and y1 == foody:
            time += dtime
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        if show:
            clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 