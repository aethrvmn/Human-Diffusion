import numpy as np

class Diffuser:

    def __init__(self, step, x_distance, y_distance):

        self.dx = step
        self.x = x_distance
        self.y = y_distance
        self.surface = np.zeros([x_distance,y_distance])

        def parameters(self, constant):

            self.dt = self.dx**2 / (4 * constant)
            self.gamma = (constant*self.dt)/(self.dx**2)
