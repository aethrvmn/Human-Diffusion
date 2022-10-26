import numpy as np
import matplotlib.pyplot as plt

from earth import Earth

class QLearn:

    def __init__(self, ):
        #Generate the map
        self.stage = Earth('earth.jpg')
        self.stage.black_and_white('newPixels.csv', 'pure-bw-earth.jpg')
        self.stage.generate_image('pure-bw-earth.jpg')

        #These are the available actions
        self.actions = ['west', 'east', 'north', 'south']
        q_values = np.random.uniform(size=(self.stage.height,self.stage.width, len(self.actions)))


    def make_reward_map():
        self.reward_map = -1*np.ones(shape=(stage.height,stage.width))
        self.reward_map[np.where(stage.map > 0)] = -200

    def spawn():
        self.col = np.random.randint(680, 690)
        self.row = np.random.randint(1105, 1115)
        return self

    def choose_action(height, width, epsilon):
        if np.random.random() < epsilon:
            self.move = np.argmax(q_values[height, width])
        else:
            self.move = np.random.randint(4)
        return self

    def new_location(height, width, action):
        self.new_width = width
        self.new_height = height

        if self.actions[action] == 'west':
            if width == 0:
                self.new_width = self.stage.width
            else:
                self.new_width = width - 1

        if self.actions[action] == 'east':
            if width == self.stage.width:
                self.new_width = 0
            else:
                self.new_width = width + 1

        if self.actions[action] == 'north' and height > 1:
            self.new_height = height - 1

        if self.actions[action] == 'south' and height < self.stage.height:
            self.new_height = height + 1

        return self
