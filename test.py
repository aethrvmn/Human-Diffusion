import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from diffusion import Diffuser

walk = Diffuser(0.5, 3, 3, 10)
walk.paths()

# for i in np.arange(len(walk.walks[0])):
#     plt.plot(walk.walks[i])
# ims = []
peos = np.array(walk.walks)
print(peos)
plt.plot(peos[0,:)
# fig = plt.figure()
# ax = fig.add_subplot()
#
# lines = [ax.plot([], [])[0] for _ in walk.walks]
# # for i in np.arange(len(walk.journey)):
# #     img = plt.plot(walk.journey[:i, 0], walk.journey[:i, 1], animated=True)
# #     ims.append([img])
#
# ani = animation.FuncAnimation(fig, walk.update_lines, walk.num_steps, fargs=(walk.walks, lines), interval=100)
#
plt.show()
# def motion(t, x=0, y=1):
#     mu, sigma = x*t, y*t,
#     val = np.random.normal(mu, sigma)
#
#     return(val)
#
# time= np.arange(100)
# pathx = np.zeros((len(time), 2))
#
#
# for i in np.arange(len(time)):
#     for j in np.arange(len(time)):
#         pathx[i,j] = pathx[i,j-1]+motion(time[i])
# print(pathx)
#
#
# plt.plot(pathx[1], pathx[2])
# plt.show()
