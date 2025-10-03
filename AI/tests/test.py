# Step 3: Train an RL agent with PPO, here a minimal example with stable-baselines3
from stable_baselines3 import PPO
import gymnasium as gym

# Create environment
env = gym.make("CarRacing-v3", render_mode=None)  # no rendering during training

# Create PPO model
model = PPO("CnnPolicy", env, verbose=1)

# Train for 100,000 timesteps (takes a while, start small if testing)
model.learn(total_timesteps=10000) 

# Save the model
model.save("ppo_carracing")
