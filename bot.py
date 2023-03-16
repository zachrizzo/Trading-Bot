import time
import torch
import numpy as np

from network.dqnagent import DQNAgent
from network.replaybuffer import ReplayBuffer

import alpaca_trade_api as tradeapi

class Bot():

    def __init__(self, api, symbols, window_size, batch_size, epsilon, epsilon_decay, epsilon_min, learning_rate, gamma, memory_size):
        self.api = api
        self.symbols = symbols
        self.window_size = window_size
        self.stock_price_memory = []
        self.batch_size = batch_size
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.memory_size = memory_size
        self.memory = ReplayBuffer(self.memory_size)
        self.model = DQNAgent(self.window_size, 3, self.learning_rate, self.gamma, self.epsilon, self.epsilon_decay, self.epsilon_min)
    
    def get_crypto_data(self):
        crypto_data = self.api.get_latest_crypto_trades(self.symbols)
        print(crypto_data)
        return crypto_data

    # def buy(self):
    #     # preparing market order
    #     market_order_data = MarketOrderRequest(
    #                         symbol="SPY",
    #                         qty=0.023,
    #                         side=OrderSide.BUY,
    #                         time_in_force=TimeInForce.DAY)

    #     # Market order
    #     market_order = trading_client.submit_order(
    #                     order_data=market_order_data)

    def act(self, state):
        return self.model.act(state)
    
    def train(self):
        if len(self.memory.buffer) < self.batch_size:
            return
        self.model.train(self.memory, self.batch_size)

    def remember(self, state, action, reward, next_state, done):
        self.memory.add(state, action, next_state, reward, done)

    def get_state(self, data, t, n):
        d = t - n
        block = data[d:t+1] if d >= 0 else -d * [data[0]] + data[0:t+1]
        res = []
        for i in range(n):
            res.append(block[i+1] - block[i])
        return np.array([res])

    def get_reward():
        pass
    
    def run(self):
        
        data = self.get_crypto_data()
        print(self.api.get_position(self.symbols))
        l = len(data) - 1
        state = self.get_state(data, 0, self.window_size)
        total_profit = 0
        self.model.q_network.train()

        for t in range(l):
            action = self.act(state)
            next_state = self.get_state(data, t+1, self.window_size)
            reward = 0
            if action == 1:
                # buy(self.symbol)
                print("Buy")
            elif action == 2:
                # sell(self.symbol, self.api)
                print("Sell")
            else:
                print("Hold")
            done = True if t == l - 1 else False
            self.remember(state, action, reward, next_state, done)
            state = next_state
            self.train()
            if done:
                print("--------------------------------")
                print("Total Profit: {}".format(total_profit))
                print("--------------------------------")
        self.model.q_network.eval()
        return total_profit
    
    def load(self, name):
        self.model.q_network.load_state_dict(torch.load(name))

    def save(self, name):
        torch.save(self.model.q_network.state_dict(), name)    