""" 使用不同的配置文件以适配生产&测试环境

python your_code.py --config-name=test
python your_code.py --config-name=prod
"""

import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="./conf", config_name="test", version_base=None)
def main(cfg: DictConfig):
    # 打印原始配置
    print("Original config:")
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    main()
