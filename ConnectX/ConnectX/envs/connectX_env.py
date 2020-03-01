import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ConnectXEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  self.playableSlots = []

  def __init__(self, n_row, n_col):
    super(CustomEnv, self).__init__()
    self.board = np.zeros((n_row, n_col))
    self.n_row = n_row
    self.n_col = n_col
    #self.viewer = None
    self.playableSlots = [(1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5)]

    self.action_space = spaces.Discrete(n_col) 
    self.observation_space = spaces.Box(low=0, high=2, shape=(n_row, n_col), dtype=np.uint8)


  def step(self, action):
    play(joueur = 1, action)
    play(joueur = 2, random???)

  def reset(self):
    #self._check_levelup()
    self.last_action = None
    self.last_reward = 0

    self.board = np.zeros((self.n_row, self.n_col))
    self.time = 0
    self.target = self.target_from_input_data(self.input_data)

    return self._get_obs()


  def render(self, mode='human'):
    ...
  
