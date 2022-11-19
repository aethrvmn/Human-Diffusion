import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class QLearner:

    def __init__(self, stage):
        self.stage = stage
        self.actions = ['west', 'east', 'north', 'south']
        self.q_values = np.random.uniform(size=(stage.height,stage.width,len(self.actions)))
        self.reward_per_episode = np.array([])

    def spawn(self, column, row):
        col = np.random.randint(column[0], column[1])
        row = np.random.randint(row[0], row[1])
        return col, row

    def next_action(self, current_height, current_width, epsilon):
        if np.random.random() < epsilon:
            move = np.argmax(self.q_values[current_height, current_width])
        else:
            move = np.random.randint(4)
        return move


    def next_location(self, height, width, action):
        new_width = width
        new_height = height

        if actions[action] == 'west' and width > -1:
            new_width = width - 1

        if actions[action] == 'east' and width < self.stage.width - 1:
            new_width = width + 1

        if actions[action] == 'north' and height > 1:
            new_height = height -1

        if actions[action] == 'south' and height < self.stage.height:
            new_height = height +1

        return new_height, new_width

    def make_reward_map(self):
        reward_map = -np.ones(shape=(stage.height,stage.width))
        reward_map[np.where(stage.map > 0)] = -10
        reward_map[0:3, 0:3] = -15

        #Arabian bridge
        reward_map[550:620, 345:390] = -1
        reward_map[500:550, 405:435] = -1
        reward_map[565:575, 400:410] = 1

        #Iran
        reward_map[515:525, 435:445] = 2

        #India
        reward_map[520:530, 490:500] = 3
        reward_map[600:610, 525:535] = 4
        reward_map[530:540, 580:590] = 5

        #Siamese bridge
        reward_map[585:595, 660:670] = 6
        reward_map[650:680, 655:670] = -1
        reward_map[675:690, 665:670] = 7

        #Indonesian bridge 1
        reward_map[690:705, 670:680] = -1
        reward_map[705:710, 690:700] = 8


        #Indonesian bridge 2
        reward_map[705:725, 720:800] = -1
        reward_map[705:795, 720:800] = -1
        reward_map[775:780, 1550:1555] = 9

        #Australia
        reward_map[780:810, 780:810] = 15
