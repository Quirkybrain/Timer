import tkinter as tk
import MainPage
import CountDownTimeSetPage
from tkinter import messagebox


def timer_rule(second_num, minute_num, hour_num):
    # if second_num == -1 and minute_num != 0:
    #     minute_num -= 1
    #     second_num = 59
    # if minute_num == -1 and hour_num != 0:
    #     hour_num -= 1
    #     minute_num = 59
    # if hour_num == 0 and minute_num == 0 and second_num == -1:
    #     hour_num = 0
    #     minute_num = 0
    #     second_num = 0
    # if second_num == -1 and minute_num == 0 and hour_num != 0:
    #     hour_num -= 1
    #     minute_num = 59
    #     second_num = 59
    if second_num == -1:
        if minute_num > 0:
            minute_num -= 1
            second_num = 59
        elif hour_num > 0:
            hour_num -= 1
            minute_num = 59
            second_num =59
        else:
            hour_num = minute_num = second_num = 0
    return second_num, minute_num, hour_num


def out_put_format(second_num, minute_num, hour_num):
    if second_num < 10:
        str_second = "0" + str(second_num)
    else:
        str_second = str(second_num)

    if minute_num < 10:
        str_minute = "0" + str(minute_num)
    else:
        str_minute = str(minute_num)

    if hour_num < 10:
        str_hour = "0" + str(hour_num)
    else:
        str_hour = str(hour_num)
    return str_second, str_minute, str_hour


class CountDown(tk.Frame, ):
    """一个倒计时器"""

    def __init__(self, hour_setting, minute_setting, second_setting, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.time_is_running = False  # 记录是否开始倒计时

        self.initial_fg_color = "#305F72"
        self.hour = hour_setting
        self.minute = minute_setting
        self.second = second_setting
        self.start_second, self.start_minute, self.start_hour = out_put_format(second_num=self.second,
                                                                               minute_num=self.minute,
                                                                               hour_num=self.hour)
        self.countdown_page()
        #print(self.start_hour, self.start_minute, self.start_second)
    def countdown_page(self):
        # 显示功能名称
        self.name_label = tk.Label(self, text="倒计时", font=("微软雅黑", 20), fg="#9999FF", bg="#66FFFF")
        self.name_label.place(relx=0.025, rely=0, relheight=0.1, relwidth=0.95)

        # 显示小时
        self.hours_label = tk.Label(self, text=self.start_hour, font=("微软雅黑", 80), fg="#305F72", bg="#CCCCFF")
        self.hours_label.place(relx=0.025, rely=0.1, relheight=0.7, relwidth=0.25)

        # 显示分钟
        self.minutes_label = tk.Label(self, text=self.start_minute, font=("微软雅黑", 80), fg="#305F72", bg="#FFCCFF")
        self.minutes_label.place(relx=0.375, rely=0.1, relheight=0.7, relwidth=0.25)

        # 显示秒
        self.seconds_label = tk.Label(self, text=self.start_second, font=("微软雅黑", 80), fg="#305F72", bg="#FFCCCC")
        self.seconds_label.place(relx=0.725, rely=0.1, relheight=0.7, relwidth=0.25)

        # 第一个分隔符
        self.separator_1_label = tk.Label(self, text=":", font=("微软雅黑", 100), fg="#305F72", bg="#E6CCFF")
        self.separator_1_label.place(relx=0.275, rely=0.1, relheight=0.7, relwidth=0.1)

        # 第二个分隔符
        self.separator_2_label = tk.Label(self, text=":", font=("微软雅黑", 100), fg="#305F72", bg="#FFCCE6")
        self.separator_2_label.place(relx=0.625, rely=0.1, relheight=0.7, relwidth=0.1)

        # 点击进入返回时钟
        self.timer_button = tk.Button(self, text="返回", command=self.back_to_clock_page)
        self.timer_button.place(relx=0.025, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击关闭程序
        self.exit_button = tk.Button(self, text="关闭", command=self.close_window)
        self.exit_button.place(relx=0.875, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击开始计时
        self.start_button = tk.Button(self, text="开始", command=self.start_counting)
        self.start_button.place(relx=0.175, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击结束计时
        self.stop_button = tk.Button(self, text="暂停", command=self.stop_counting)
        self.stop_button.place(relx=0.325, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击重新设置时间
        self.set_button = tk.Button(self, text="设置", command=self.open_countdown_setting_page)
        self.set_button.place(relx=0.475, rely=0.85, relheight=0.1, relwidth=0.1)

        # 点击重置时间
        self.reset_button = tk.Button(self, text="重置", command=self.reset_times)
        self.reset_button.place(relx=0.625, rely=0.85, relheight=0.1, relwidth=0.1)


    def close_window(self):
        # 结束程序
        self.master.destroy()

    def back_to_clock_page(self):
        if not self.time_is_running:
            self.destroy()
            self.page_clock = MainPage.Clock(self.master)
        else:
            messagebox.showinfo("禁止", "正在计时")

    def open_countdown_setting_page(self):
        # 切换至Count Down Setting界面
        if not self.time_is_running:
            self.page_countdown_setting = CountDownTimeSetPage.CountDownTimeSetting(self.master)
            self.destroy()
        else:
            messagebox.showinfo("禁止", "正在计时")

    def start_counting(self):
        # 开始计时
        if not self.time_is_running:
            self.time_is_running = True
            self.second += 1
            self.update_times()
        else:
            messagebox.showinfo("禁止", "正在计时")

    def stop_counting(self):
        # 结束计时
        if self.time_is_running:
            self.time_is_running = False

    # def set_times(self):
    #     if not self.time_is_running:
    #         self.hours_lable.config(fg="#305F72", text="00")
    #         self.minutes_lable.config(fg="#305F72", text="00")
    #         self.seconds_lable.config(fg="#305F72", text="00")

    def reset_times(self):
        if not self.time_is_running:
            self.hours_label.config(text=self.start_hour, fg=self.initial_fg_color)
            self.minutes_label.config(text=self.start_minute, fg=self.initial_fg_color)
            self.seconds_label.config(text=self.start_second, fg=self.initial_fg_color)
            self.hour = int(self.start_hour)
            self.minute = int(self.start_minute)
            self.second = int(self.start_second)
        else:
            messagebox.showinfo("禁止", "正在计时")

    def time_out_sign(self):
        messagebox.showinfo("倒计时", "时间到!!!!")

    def update_times(self):

        if self.time_is_running:

            self.second -= 1
            self.second, self.minute, self.hour = timer_rule(second_num=self.second, minute_num=self.minute,
                                                             hour_num=self.hour)
            self.str_second, self.str_minute, self.str_hour = out_put_format(second_num=self.second,
                                                                             minute_num=self.minute, hour_num=self.hour)
            if self.second <= 5 and self.minute == 0 and self.hour == 0:
                self.hours_label.config(fg="red")
                self.minutes_label.config(fg="red")
                self.seconds_label.config(fg="red")
            if self.second == 0 and self.minute == 0 and self.hour == 0:
                self.time_is_running = False
                self.after(1000, self.time_out_sign)
            self.hours_label.config(text=self.str_hour)
            self.minutes_label.config(text=self.str_minute)
            self.seconds_label.config(text=self.str_second)
            self.after(1000, self.update_times)
