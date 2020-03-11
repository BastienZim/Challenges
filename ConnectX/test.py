from kaggle_environments import evaluate, make, utils
import gym

env = make("connectx", debug=True)
#env.render()

def my_agent(observation, configuration):
    from random import choice
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])


env.reset()
# Play as the first agent against default "random" agent.
#env.run([my_agent, "random"])
#env.render()

def mean_reward(rewards):
    return sum(r[0] for r in rewards) / sum(r[0] + r[1] for r in rewards)


class ConnectX(gym.Env):

    def __init__(self):
        self.env = make("connectx", debug=True)
        self.trainer = self.env.train([None, "random"])

        # Define required gym fields (examples):
        config = self.env.configuration
        self.action_space = gym.spaces.Discrete(config.columns)
        self.observation_space = gym.spaces.Discrete(config.columns * config.rows)

    def step(self, action):
        return self.trainer.step(action)

    def reset(self):
        return self.trainer.reset()

    def render(self, **kwargs):
        return self.env.render(**kwargs)

env = ConnectX()

done = False
obs = env.reset()
i=0
while not done:
    # Choose first available empty column as the action.
    action = [i for i in range(len(obs.board)) if obs.board[i] == 0][0]
    obs, reward, done, info = env.step(action)
    print(obs, reward, done, info)
    i+=1
    if(i==2):
        break
env.render()







