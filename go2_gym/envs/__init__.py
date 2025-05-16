from go2_gym import GO2_GYM_ROOT_DIR, GO2_GYM_ENVS_DIR


from .go2.go2_config import GO2RoughCfg, GO2RoughCfgPPO
from .base.legged_robot import LeggedRobot




import os 
from go2_gym.utils.task_registry import task_registry


task_registry.register("go2rough", LeggedRobot, GO2RoughCfg(), GO2RoughCfgPPO())




