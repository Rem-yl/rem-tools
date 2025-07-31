"""
定时任务, 打开metabase报表
"""
import subprocess
import tkinter as tk
from tkinter import messagebox

# 要打开的网址
url = "https://adalgo-metabase.ams.op-mobile.opera.com/dashboard/7-lazada-allegro?tab=3-tab-1"

# 弹窗提示是否打开


def ask_to_open():
    root = tk.Tk()
    root.withdraw()  # 不显示主窗口
    answer = messagebox.askyesno("打开报表", "是否打开 Lazada Allegro Metabase 报表？")
    root.destroy()

    if answer:
        subprocess.run(["open", "-a", "Microsoft Edge", url])


if __name__ == "__main__":
    ask_to_open()
