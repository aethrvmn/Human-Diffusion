import numpy as np

class Diffuser:

    def __init__(self, step, x_distance, y_distance, number_of_particles, starting_position = [0,0]):
        self.start_pos = starting_position
        self.num_par = number_of_particles
        self.dx = step
        self.x = x_distance
        self.y = y_distance
        self.num_steps = int(self.x/self.dx)
        self.surface = np.zeros([x_distance,y_distance])


    def parameters(self, constant):
        self.dt = self.dx**2 / (4 * constant)
        self.gamma = (constant*self.dt)/(self.dx**2)
        return self

    def walk(self):
        self.length = np.random.uniform(-self.dx, self.dx, size = (self.num_steps,2))
        self.length[0,:]=0
        self.journey = self.start_pos + np.cumsum(self.length, axis = 0)
        return self

    def paths(self):
        self.walks = []
        for index in range(int(self.num_par)):
            self.walk()
            self.walks.append(self.journey)
