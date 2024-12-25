import argparse


def main():
    # 创建ArgumentParser对象，添加描述
    parser = argparse.ArgumentParser(
        description="This is a sample program to demonstrate how to print all parameter descriptions.")

    # 添加参数
    parser.add_argument('--name', type=str, help='Your name')
    parser.add_argument('--age', type=int, help='Your age')
    parser.add_argument('--city', type=str, help='Your city of residence')

    # 打印所有参数的帮助信息
    print("Available arguments and their descriptions:")
    parser.print_help()  # 打印所有参数及其描述

    # 解析命令行参数
    args = parser.parse_args()

    # 显示用户输入的内容
    if args.name and args.age and args.city:
        print(f"Hello, {args.name}! You are {args.age} years old and live in {args.city}.")
    else:
        print("Please provide your name, age, and city.")


if __name__ == "__main__":
    main()
