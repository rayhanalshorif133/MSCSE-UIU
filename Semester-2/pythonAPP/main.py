import pandas as pd
import numpy as np

# Step 1: Read the dataset
csv_file_path = './student_activity_dataset.csv'  # Update the path
data = pd.read_csv(csv_file_path)

# Display the DataFrame
print("Student Activity Dataset:")
print(data)

# Step 2: Define the Environment
class StudentEnvironment:
    def __init__(self, data):
        self.data = data
        self.current_index = 0
        self.action_space = [0, 1]  # Actions: 0 = Decrease study time, 1 = Increase study time

    def reset(self):
        self.current_index = 0  # Start from the first student
        return self.get_state()

    def get_state(self):
        row = self.data.iloc[self.current_index]
        return np.array([row['Study_Time (hrs)'], row['Attendance (%)'], row['Extracurricular (hrs)'], row['Motivation (1-10)']])

    def step(self, action):
        # Apply action to the current student
        current_state = self.get_state()
        if action == 1:  # Increase study time
            self.data.at[self.current_index, 'Study_Time (hrs)'] += 1
        else:  # Decrease study time
            self.data.at[self.current_index, 'Study_Time (hrs)'] -= 1

        # Calculate reward based on the updated exam score
        reward = self.calculate_reward()
        done = self.is_done()
        return self.get_state(), reward, done

    def calculate_reward(self):
        # Reward based on exam score (here we use the actual value)
        return self.data.at[self.current_index, 'Reward (Exam Score)']

    def is_done(self):
        self.current_index += 1
        return self.current_index >= len(self.data)

# Step 3: Define the Q-learning Agent
class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9):
        self.q_table = np.zeros((len(data), 2))  # 2 actions
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor

    def choose_action(self, state_index):
        return np.argmax(self.q_table[state_index])  # Exploit learned values

    def update_q_value(self, state_index, action, reward, next_state_index):
        best_future_q = np.max(self.q_table[next_state_index])
        self.q_table[state_index, action] += self.alpha * (reward + self.gamma * best_future_q - self.q_table[state_index, action])

# Step 4: Training the RL Model
env = StudentEnvironment(data)
agent = QLearningAgent()


# Function to predict student performance
def predict_student_performance(agent, student_data):
    # Prepare the state from the student's features
    state = np.array([
        student_data['Study_Time (hrs)'],
        student_data['Attendance (%)'],
        student_data['Extracurricular (hrs)'],
        student_data['Motivation (1-10)']
    ])

    # Assuming you have some mapping from features to state index
    state_index = data.index[data['Student_ID'] == student_data['Student_ID']][0]  # Get the index of the student

    # Step 2: Choose the action with the highest Q-value for this state
    action = np.argmax(agent.q_table[state_index])

    # Apply action to predict new state
    if action == 1:  # Increase study time
        predicted_study_time = state[0] + 1
    else:  # Decrease study time
        predicted_study_time = max(0, state[0] - 1)

    # The exam score can be influenced by the new study time
    predicted_exam_score = (
        predicted_study_time * 10 +  # Simple linear relation for illustration
        state[1] * 0.5 +  # Weighting attendance
        state[2] * 0.3 +  # Weighting extracurricular activities
        state[3] * 2  # Weighting motivation
    )

    return predicted_study_time, predicted_exam_score

# Example of predicting for a specific student
example_student_data = {
    'Student_ID': 1,  # Use the correct ID
    'Study_Time (hrs)': 5,
    'Attendance (%)': 90,
    'Extracurricular (hrs)': 2,
    'Motivation (1-10)': 8
}

predicted_study_time, predicted_exam_score = predict_student_performance(agent, example_student_data)

print(f"Predicted Study Time: {predicted_study_time} hours")
print(f"Predicted Exam Score: {predicted_exam_score:.2f}")

