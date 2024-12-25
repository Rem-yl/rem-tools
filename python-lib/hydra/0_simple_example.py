""" hydra的一个通用案例, 读取配置文件 

可以在命令行使用: 
    - python your_code.py optimizer.name=adam   来修改已有的参数
    - python your_code.py +optimizer.gamma=0.1  添加新的参数
    
    - python your_code.py --multirun optimizer.alpha=0.1, 0.2, 0.5 来启动多组实验
    - python your_code.py --multirun optimizer.alpha=range(0.01, 0.1, 0.01) 启动参数范围实验
"""


import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path="./", config_name="default")
def get_opimizer_param(cfg: DictConfig):

    print(f"Config: \n {OmegaConf.to_yaml(cfg)}")
    # 将 universal 的配置融合进所有配置中
    OmegaConf.set_struct(cfg, False)
    global_cfg = cfg.pop("universal")
    for key, value in cfg.items():
        cfg[key] = OmegaConf.merge(global_cfg, value)
    OmegaConf.set_struct(cfg, True)

    optimizer_cfg = cfg.optimizer

    print(optimizer_cfg)


if __name__ == "__main__":
    get_opimizer_param()
