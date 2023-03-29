import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class HumanMigration:
    def __init__(self, stage, num_episodes = 2000, num_timeline = 500):
        self.stage = stage
        self.actions = ['west', 'east', 'north', 'south']
        self.q_values = np.random.uniform(-1, 1, size=(stage.height, stage.width, len(self.actions)))
        self.reward_map = np.zeros(shape=(stage.height, stage.width))
        self.real_map = np.ones(shape=(stage.height, stage.width)) * 10
        self.initialize_reward_map()
        self.timeline = np.arange(0, 500)
        self.episodes = np.arange(0, 2000)

    def initialize_reward_map(self):
        self.reward_map[np.where(self.stage.map > 0)] = -10
        self.reward_map[:10, :] = -15
        self.reward_map[610:, :] = -15
        self.reward_map[:, 720:] = -15
        self.reward_map[:, :10] = -15

        # Arabian bridge
        self.reward_map[350:388, 250:282] = 0
        self.reward_map[300:340, 290:315] = 0

        # Indonesian bridge
        self.reward_map[417:433, 485:495] = 0
        self.reward_map[450:455, 495:505] = 0
        self.reward_map[430:465, 525:530] = 0
        self.reward_map[460:465, 525:645] = 0
        self.reward_map[460:505, 525:605] = 0

        # Bering Straight
        self.reward_map[30:60, 580:610] = 50
        # Australia
        self.reward_map[510:540, 580:610] = 50

        self.real_map[np.where(self.stage.map > 0)] = -10

    def starting_area(self, column, row):
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

        if self.actions[action] == 'west' and width > -1:
            new_width = width - 1

        if self.actions[action] == 'east' and width < self.stage.width - 1:
            new_width = width + 1

        if self.actions[action] == 'north' and height > 1:
            new_height = height - 1

        if self.actions[action] == 'south' and height < self.stage.height:
            new_height = height + 1
        return new_height, new_width

    def run_simulation(self):
        reward_per_episode = np.zeros(len(self.episodes))
        lifetime = np.zeros(len(self.episodes))

        for episode in tqdm(self.episodes):
            rewards, year = self.run_episode(episode)
            reward_per_episode[episode] = np.mean(rewards)
            lifetime[episode] = year

        # Save the reward_per_episode and lifetime data to .npy files
        np.save('Metrics/reward_per_episode.npy', reward_per_episode)
        np.save('Metrics/lifetime.npy', lifetime)
        np.save('Metrics/q_table.npy', self.q_values)

        return reward_per_episode, lifetime

    def run_episode(self, episode):
        epsilon = 0.7
        discount_factor = 0.3
        learning_rate = 1

        rewards = np.zeros(len(self.timeline))

        if episode >= 195000:
            self.set_destabilization_rewards()

        old_height, old_width = 400, 230
        height, width = self.starting_area([old_height-5, old_height+5], [old_width-5, old_width+5])

        for year in self.timeline:
            try:
                action = self.next_action(height, width, epsilon)
                old_height, old_width = height, width
                height, width = self.next_location(height, width, action)

                reward = self.reward_map[height, width]
                rewards[year] = reward

                self.update_q_values(old_height, old_width, action, height, width, reward, discount_factor, learning_rate)

                if self.reward_map[old_height, old_width] > 0:
                    self.reward_map[old_height, old_width] = 0

                self.real_map[old_height, old_width] = 5

            except IndexError as e:
                break

            if year == self.timeline[-1]:
                return rewards, year

            if self.reward_map[old_height, old_width] <= -10 and self.reward_map[height, width] <= -10:
                return rewards, year
                break


    def load_reward_per_episode_data(self):
        # Replace 'reward_per_episode.npy' with the path to the saved reward_per_episode data file
        reward_per_episode = np.load('Metrics/reward_per_episode.npy')
        return reward_per_episode

    def load_lifetime_data(self):
        # Replace 'lifetime.npy' with the path to the saved lifetime data file
        lifetime = np.load('Metrics/lifetime.npy')
        return lifetime

    def load_q_table(self):
        self.q_values = np.load('Metrics/q_table.npy')


    def set_destabilization_rewards(self):
        # India
        self.reward_map[390, 388] = 20
        # New Guinea Papua
        self.reward_map[455, 650] = 20
        # Brunei
        self.reward_map[425, 540] = 20
        # Australia
        self.reward_map[510:540, 580:610] = 50

    def update_q_values(self, old_height, old_width, action, height, width, reward, discount_factor, learning_rate):
        old_q_value = self.q_values[old_height, old_width, action]
        temporal_difference = reward + (discount_factor * np.max(self.q_values[height, width])) - old_q_value

        new_q_value = old_q_value + (learning_rate * temporal_difference)
        self.q_values[old_height, old_width, action] = new_q_value

    def plot_results(self, reward_per_episode, lifetime):
        avg_reward, avg_life = self.calculate_averages(reward_per_episode, lifetime)

        self.plot_migration_map()
        self.plot_avg_reward(avg_reward)
        self.plot_avg_lifetime(avg_life)

    def calculate_averages(self, reward_per_episode, lifetime):
        avg_reward = np.array([])
        avg_life = np.array([])
        pp = int(len(self.episodes) / 10)

        for i in np.arange(len(self.episodes)):
            if i % pp == 0 and i > 0:
                avg_reward = np.append(avg_reward, np.mean(reward_per_episode[i-pp:i]))
                avg_life = np.append(avg_life, np.mean(lifetime[i-pp:i]))

        return avg_reward, avg_life

    def plot_migration_map(self):
        plt.figure(figsize=(10, 10))
        plt.ylabel('Latitude')
        plt.xlabel('Longitude')
        plt.xticks([])
        plt.yticks([])
        plt.imshow(self.real_map, cmap='ocean_r')
        plt.savefig('Metrics/Images/migration_exploration.jpg')
        plt.show()

    def plot_avg_reward(self, avg_reward):
        plt.figure(figsize=(10, 5))
        plt.title("Average Reward")
        plt.xlabel('Episodes')
        plt.plot(avg_reward)
        plt.savefig('Metrics/Images/avg_reward.jpg')
        plt.show()

    def plot_avg_lifetime(self, avg_life):
        plt.figure(figsize=(10, 5))
        plt.title("Average Lifetime of Group")
        plt.xlabel('Episodes')
        plt.ylabel('Generations')
        plt.plot(avg_life)
        plt.savefig('Metrics/Images/avg_lifetime.jpg')
        plt.show()
