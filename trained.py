from human_migration import HumanMigration
from earth import Earth
stage = Earth()
stage.generate_image('Images/pure-bw-earth.jpg')

migration_simulation = HumanMigration(stage, num_episodes = 1)

# Load the Q table
migration_simulation.load_q_table()

# Load the reward_per_episode and lifetime data from the trained model
reward_per_episode = migration_simulation.load_reward_per_episode_data()
lifetime = migration_simulation.load_lifetime_data()

reward_per_episode, lifetime = migration_simulation.run_simulation()
# Display the results
migration_simulation.plot_results(reward_per_episode, lifetime)
