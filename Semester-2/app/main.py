import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import random


# Specify the file path
file_path = './file.csv'  # Replace with your actual file path

df = pd.read_csv(file_path)

# Define Q-learning parameters
num_episodes = 1000  # Number of episodes for training
learning_rate = 0.1  # Alpha
discount_factor = 0.9  # Gamma
exploration_rate = 1.0  # Epsilon
max_exploration_rate = 1.0
min_exploration_rate = 0.01
exploration_decay_rate = 0.001


# Initialize Q-table
state_size = len(df)
action_size = 2  # For simplicity: 0 = decrease study time, 1 = increase study time
Q_table = np.zeros((state_size, action_size))

# Define the action space
def take_action(state):
    if random.uniform(0, 1) < exploration_rate:  # Explore
        return random.choice(range(action_size))
    else:  # Exploit
        return np.argmax(Q_table[state])

# Update the Q-table
def update_Q_table(state, action, reward, next_state):
    Q_table[state, action] = Q_table[state, action] + learning_rate * (reward + discount_factor * np.max(Q_table[next_state]) - Q_table[state, action])

# Simulate the environment
def get_reward(state, action):
    if action == 0:  # Decrease study time
        return -df['Reward'][state] * 0.1  # Assuming reducing study time negatively impacts scores
    elif action == 1:  # Increase study time
        return df['Reward'][state] * 0.1  # Assuming increasing study time positively impacts scores

# Training the Q-learning agent
for episode in range(num_episodes):
    for state in range(state_size):
        action = take_action(state)
        reward = get_reward(state, action)
        next_state = state + 1 if state + 1 < state_size else state  # Move to next student or stay
        update_Q_table(state, action, reward, next_state)

    # Decay exploration rate
    exploration_rate = max(min_exploration_rate, exploration_rate * (1 - exploration_decay_rate))

# Visualize the Q-table
plt.imshow(Q_table, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Q-Table Heatmap')
plt.xlabel('Actions (0: Decrease Study Time, 1: Increase Study Time)')
plt.ylabel('Student Index')
plt.show()

# Print the Q-table
print("Final Q-Table:")
print(Q_table)