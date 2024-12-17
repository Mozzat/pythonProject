'''
Author: mozzat taogroups@163.com
Date: 2024-12-09 15:15:47
LastEditors: mozzat taogroups@163.com
LastEditTime: 2024-12-17 15:12:01
FilePath: /pythonProject/app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#coding=utf-8
import tkinter as tk
from tkinter import filedialog
import home
import SQLManager
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap import Button

def open_folder():
    folder_selected = filedialog.askopenfilename()
    if folder_selected:
        print(f"选择的文件夹: {folder_selected}")
        home.queryFileReadData(folder_selected)

def open_productList():
    folder_selected = filedialog.askopenfilename()
    if folder_selected:
        print(f"选择的文件夹: {folder_selected}")
        SQLManager.updateProductList(folder_selected)

def main():
    # 创建主窗口
    root = tk.Tk()
    root.title("桃桃子")
    root.geometry("600x600")  # 设置窗口大小为 600x600

    # 创建按钮
    button = tk.Button(root, text="选择文件夹", command=open_folder)
    button.pack(pady=100)

    # 将按钮放置在窗口中央
    window_width = 600
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # 运行主循环
    root.mainloop()

if __name__ == "__main__":
    main()