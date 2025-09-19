import tkinter as tk
from tkinter import messagebox

import MainPage
import CountDownPage


class CountDownTimeSetting(tk.Frame):
    """一个电子时钟"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.countdown_time_setting_page()

    def countdown_time_setting_page(self):

        # 输入小时
        self.hour_entry = tk.Entry(self, validate="key", font=("微软雅黑", 25), bg="#CCCCFF")
        self.hour_entry.place(relx=0.5, rely=0.2, relwidth=1 / 6, relheight=0.15, )

        # 输入分钟
        self.minute_entry = tk.Entry(self, validate="key", font=("微软雅黑", 25), bg="#FFCCFF")
        self.minute_entry.place(relx=0.5, rely=0.4, relwidth=1 / 6, relheight=0.15)

        # 输入秒
        self.second_entry = tk.Entry(self, validate="key", font=("微软雅黑", 25), bg="#FFCCCC")
        self.second_entry.place(relx=0.5, rely=0.6, relwidth=1 / 6, relheight=0.15)

        # 提示：输入小时
        self.hour_label = tk.Label(self, text="时", font=("微软雅黑", 20))
        self.hour_label.place(relx=1 / 3, rely=0.2, relwidth=1 / 6, relheight=0.15)

        # 提示：输入分钟
        self.minute_label = tk.Label(self, text="分", font=("微软雅黑", 20))
        self.minute_label.place(relx=1 / 3, rely=0.4, relwidth=1 / 6, relheight=0.15)

        # 提示：输入秒
        self.second_label = tk.Label(self, text="秒", font=("微软雅黑", 20))
        self.second_label.place(relx=1 / 3, rely=0.6, relwidth=1 / 6, relheight=0.15)

        # 确认
        self.start_button = tk.Button(self, text="确认", command=self.get_entry_value_and_open_countdown_page)
        self.start_button.place(relx=0.625, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击进入返回时钟
        self.timer_button = tk.Button(self, text="返回", command=self.back_to_clock_page)
        self.timer_button.place(relx=0.025, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击关闭程序
        self.exit_button = tk.Button(self, text="关闭", command=self.close_window)
        self.exit_button.place(relx=0.875, rely=0.85, relheight=0.1, relwidth=0.1)

    def get_entry_value_and_open_countdown_page(self):
        try:
            # 获取输入值并去除前后空格
            hour_str = self.hour_entry.get().strip()
            minute_str = self.minute_entry.get().strip()
            second_str = self.second_entry.get().strip() 
            #print(hour_str, minute_str, second_str)
            #判断是否为空
            if not hour_str and not minute_str and not second_str:
                messagebox.showerror("输入错误", "时、分、秒都不能为空，请输入数字")
                return
            if not hour_str:
                hour_str = '0'
            if not minute_str:
                minute_str = '0'
            if not second_str:
                second_str = '0'
            #print(hour_str, minute_str, second_str)
            #转为整形
            hour = int(hour_str)
            minute = int(minute_str)
            second = int(second_str)
            #print(hour, minute, second)
            if hour == 0 and minute == 0 and second == 0:
                messagebox.showerror("输入错误", "时、分、秒都不能全为零，请重新输入数字")
                return
            #检查数字范围
            if not hour in range(0,60):
                messagebox.showerror("输入错误", "时必须设置在0至59")
                return
            if not minute in range(0,60):
                messagebox.showerror("输入错误", "分必须设置在0至59")
                return
            if not second in range(0,60):
                messagebox.showerror("输入错误", "秒必须设置在0至59")
                return
            self.count_down_hour_setting = hour
            self.count_down_minute_setting = minute
            self.count_down_second_setting = second
            self.page_countdown = CountDownPage.CountDown(master=self.master,
                                                          hour_setting=self.count_down_hour_setting,
                                                          minute_setting=self.count_down_minute_setting,
                                                          second_setting=self.count_down_second_setting)
            self.destroy()
        except ValueError:
            messagebox.showinfo("输入错误", "必须输入在0至59中的数字")

    def close_window(self):
        # 结束程序
        self.master.destroy()

    def back_to_clock_page(self):
        self.destroy()
        self.page_clock = MainPage.Clock(self.master)
    #
    # def open_countdown_page(self):
    #     # 切换至Count Down界面
    #     self.page_countdown = CountDownPage.CountDown(self.master, hour_setting=self.hour_setting, minute_setting=self.minute_setting, second_setting=self.second_setting)
    #     self.pack_forget()

#root = tk.Tk()
#root.title("Timer")
#root.geometry("900x300+500+400")
#app = CountDownTimeSetting(master=root)
#root.mainloop()
