import numpy as np
import os 
from datetime import datetime

import isaacgym
from go2_gym.envs import *
from go2_gym.utils import get_args,export_policy_as_jit,task_registry, Logger

import torch

def test_env(args):
    # override some parameters for testing
    env_cfg, train_cfg = task_registry.get_cfgs(name=args.task)
    # prepare environment
    env, _ = task_registry.make_env(name=args.task, args=args, env_cfg=env_cfg)
    for i in range(int(10*env.max_episode_length)):
        actions = 0.*torch.ones(env.num_envs, env.num_actions, device=env.device)
        env.step(actions)
    print("Done")


if __name__ == "__main__":
    args = get_args()
    test_env(args)