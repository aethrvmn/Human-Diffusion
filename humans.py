import numpy as np

class Human():

    def __init__(self,x0=0, y0=0):

        self.x0 = x0
        self.y0 = y0

    def gen_random_walk(self, n_step=100):

        self.x = np.ones(n_step)*self.x0
        self.y = np.ones(n_step)*self.y0

        for i in range(1,n_step):
            sample = np.random.normal()
            self.x[i] = self.x[i-1]+(sample/np.sqrt(n_step))
            sample = np.random.normal()
            self.y[i] = self.y[i-1]+(sample/np.sqrt(n_step))

        return self
