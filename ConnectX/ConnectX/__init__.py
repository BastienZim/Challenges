from gym.envs.registration import register

register(
    id='connectX-v0',
    entry_point='gym_foo.envs:ConnectX_env',)