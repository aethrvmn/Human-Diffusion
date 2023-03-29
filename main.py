from human_migration import HumanMigration
from earth import Earth
stage = Earth()
stage.generate_image('Images/pure-bw-earth.jpg')

migration_simulation = HumanMigration(stage = stage)

reward_per_episode, lifetime = migration_simulation.run_simulation()

migration_simulation.plot_results(reward_per_episode, lifetime)
