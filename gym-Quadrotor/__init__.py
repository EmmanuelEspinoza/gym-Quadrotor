from gym.envs.registration import register
register(
    id='Quadrotor-v0',
    entry_point='gym_Quadrotor.envs:QuadrotorEnv',
)
register(
    id='Quadrotor-extrahard-v0',
    entry_point='gym_Quadrotor.envs:QuadrotorExtraHardEnv',
)
