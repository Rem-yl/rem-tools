"""
Usage:
  0_example.py --data_path <data_path> --model_save_path <model_save_path> --lr <lr>
  0_example.py (-h | --help)
  0_example.py --version

Options:
  -h --help               Show this screen.
  --version               Show version.
  --data_path <data_path> 指定数据集路径
  --model_save_path <model_save_path> 指定模型保存路径
  --lr <lr>               指定学习率
"""

from docopt import docopt


def train(data_path, model_save_path, lr):
    # 这里添加你的训练逻辑
    print(f"Training with data from {data_path}")
    print(f"Model will be saved to {model_save_path}")
    print(f"Learning rate is set to {lr}")
    # 假设这是一个训练过程
    print("Training complete!")


def main():
    # 解析命令行参数
    arguments = docopt(__doc__, version="0.1")

    if arguments["--version"]:
        print("0_example.py version 0.1")
    elif arguments["--data_path"] and arguments["--model_save_path"] and arguments["--lr"]:
        data_path = arguments["--data_path"]
        model_save_path = arguments["--model_save_path"]
        lr = float(arguments["--lr"])
        train(data_path, model_save_path, lr)
    else:
        print("Invalid arguments. Use -h or --help for usage information.")


if __name__ == "__main__":
    main()
