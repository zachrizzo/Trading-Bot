import random
import numpy as np

class ReplayBuffer():
    def __init__(self, buffer_size=100000):
        self.buffer_size = buffer_size
        self.buffer = []
        self.position = 0
        
    def add(self, *args):
        experience = args
        if len(self.buffer) < self.buffer_size:
            self.buffer.append(None)
        self.buffer[self.position] = experience
        self.position = (self.position + 1) % self.buffer_size
        
    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        state, action, next_state, reward, done = zip(*batch)
        return np.array(state), np.array(action), np.array(next_state), np.array(reward), np.array(done)