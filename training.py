from earth import Earth
from learner import QLearner

stage = Earth().generate_image('pure-bw-earth.jpg')

pp = QLearner(stage)

print(pp.spawn([10,11], [12,13]))
