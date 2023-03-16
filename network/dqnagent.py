import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim

from network.qnetwork import QNetwork


class DQNAgent():
    def __init__(self, state_dim, action_dim, learning_rate=0.001, gamma=0.99, epsilon=1.0, epsilon_decay=0.9999, epsilon_min=0.01):
        self.q_network = QNetwork(state_dim, action_dim)
        self.target_network = QNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=learning_rate)
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.action_dim = action_dim
        
    def act(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.action_dim)
        state = torch.FloatTensor(state)
        q_values = self.q_network(state)
        return torch.argmax(q_values).item()
    
    def train(self, replay_buffer, batch_size):
        state, action, next_state, reward, done = replay_buffer.sample(batch_size)
        
        state = torch.FloatTensor(state)
        next_state = torch.FloatTensor(next_state)
        action = torch.LongTensor(action)
        reward = torch.FloatTensor(reward)
        done = torch.FloatTensor(done)
        
        q_values = self.q_network(state)
        next_q_values = self.target_network(next_state).detach()
        target_q_values = reward + (1 - done) * self.gamma * torch.max(next_q_values, dim=1)[0]
        target_q_values = target_q_values.unsqueeze(-1)
        q_value = torch.gather(q_values, dim=1, index=action.unsqueeze(-1))
        
        loss = nn.MSELoss()(q_value, target_q_values)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        self.update_target_network()
        self.update_epsilon()
        
    def update_target_network(self):
        tau = 0.001
        for target_param, param in zip(self.target_network.parameters(), self.q_network.parameters()):
            target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)
    
    def update_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)