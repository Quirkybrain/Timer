import tkinter as tk
import time
import TimerPage
import CountDownTimeSetPage


class Clock(tk.Frame):
    """一个电子时钟"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.clock_page()
        self.update_times()

    def clock_page(self):
        # 显示功能名称
        self.name_label = tk.Label(self, text="时钟", font=("微软雅黑", 20), fg="#9999FF", bg="#66FFFF")
        self.name_label.place(relx=0.025, rely=0, relheight=0.1, relwidth=0.95)

        # 显示小时
        self.hours_label = tk.Label(self, font=("微软雅黑", 80), fg="#305F72", bg="#CCCCFF")
        self.hours_label.place(relx=0.025, rely=0.1, relheight=0.7, relwidth=0.25)

        # 显示分钟
        self.minutes_label = tk.Label(self, font=("微软雅黑", 80), fg="#305F72", bg="#FFCCFF")
        self.minutes_label.place(relx=0.375, rely=0.1, relheight=0.7, relwidth=0.25)

        # 显示秒
        self.seconds_label = tk.Label(self, font=("微软雅黑", 80), fg="#305F72", bg="#FFCCCC")
        self.seconds_label.place(relx=0.725, rely=0.1, relheight=0.7, relwidth=0.25)

        # 第一个分隔符
        self.separator_1_label = tk.Label(self, text=":", font=("微软雅黑", 100), fg="#305F72", bg="#E6CCFF")
        self.separator_1_label.place(relx=0.275, rely=0.1, relheight=0.7, relwidth=0.1)

        # 第二个分隔符
        self.separator_2_label = tk.Label(self, text=":", font=("微软雅黑", 100), fg="#305F72", bg="#FFCCE6")
        self.separator_2_label.place(relx=0.625, rely=0.1, relheight=0.7, relwidth=0.1)

        # 点击进入Timer
        self.timer_button = tk.Button(self, text="计时器", command=self.open_timer_page)
        self.timer_button.place(relx=0.025, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击进入Count Down
        self.count_down_button = tk.Button(self, text="倒计时", command=self.open_countdown_setting_page)
        self.count_down_button.place(relx=0.175, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击关闭程序
        self.exit_button = tk.Button(self, text="关闭", command=self.close_window)
        self.exit_button.place(relx=0.875, rely=0.85, relheight=0.1, relwidth=0.1)

    def update_times(self):
        # 更新时间数据
        self.hours_label.config(text=time.strftime("%H"))
        self.minutes_label.config(text=time.strftime("%M"))
        self.seconds_label.config(text=time.strftime("%S"))
        self.after(1000, self.update_times)

    def close_window(self):
        # 结束程序
        self.master.destroy()

    def open_timer_page(self):
        # 切换至Timer界面
        self.page_timer = TimerPage.Timer(self.master)
        self.destroy()

    def open_countdown_setting_page(self):
        # 切换至Count Down Setting界面
        self.page_countdown_setting = CountDownTimeSetPage.CountDownTimeSetting(self.master)
        self.destroy()