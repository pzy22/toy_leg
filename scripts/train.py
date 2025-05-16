
import isaacgym
from go2_gym.envs import *
from go2_gym.utils import get_args, task_registry
import torch


def train(args):
    print(f"args.task: {args.task}")
    # Create the environment
    env, env_cfg = task_registry.make_env(name=args.task, args=args)
    # Create RL runner
    ppo_runner, train_cfg = task_registry.make_alg_runner(name=args.task, env=env, args=args)
    # Train the RL Agent
    ppo_runner.learn(num_learning_iterations=train_cfg.runner.max_iterations, init_at_random_ep_len=True)



if __name__ == "__main__":
    args = get_args()
    train(args)

