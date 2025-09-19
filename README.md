#Timer Application / 计时器应用
A simple and elegant timer tool built with Python's tkinter library. It features a real-time clock, a stopwatch (count-up timer), and a countdown timer with a user-friendly interface.

一个使用 Python 的 tkinter 库开发的简单而优美的计时器工具。包含实时时钟、正计时器和倒计时器三种功能，界面美观且用户友好。

Features / 功能特点
Real-time Clock / 实时时钟: Displays the current system time (HH:MM:SS).
显示当前系统时间（时:分:秒）。

Stopwatch (Timer) / 正计时器: Counts upward from 00:00:00, measuring elapsed time.
从 00:00:00 开始正向计时，测量经过的时间。

Countdown Timer / 倒计时器: Counts down from a user-set time (H:M:S) to zero, with an alert when time is up.
从用户设置的时间（时:分:秒）倒计时至零，时间到时会发出警报。

Beautiful GUI / 优美界面: Clean and colorful interface built with tkinter.
使用 tkinter 构建的简洁且色彩丰富的界面。

Intuitive Controls / 直观控制: Simple buttons for Start, Pause, Reset, and Settings.
提供开始、暂停、重置和设置等简单按钮。

Installation & Usage / 安装与使用
Prerequisites / 前提条件
Python 3.x (Developed and tested with Python 3.8+)
Python 3.x (使用 Python 3.8+ 开发和测试)

The tkinter module (usually included in standard Python installations)
tkinter 模块（通常包含在标准 Python 安装中）

Running the Application / 运行应用程序
Clone or download the project files to a directory on your computer.
将项目文件克隆或下载到您计算机上的一个目录中。

Open a terminal (Command Prompt, PowerShell, etc.) and navigate to that directory.
打开终端（命令提示符、PowerShell 等）并导航到该目录。

Run the main script:
运行主脚本：

bash
python main.py


The main clock interface will appear. Use the buttons to navigate between the Clock, Timer (Stopwatch), and Countdown functions.
主时钟界面将会出现。使用按钮在时钟、计时器（正计时）和倒计时功能之间导航。

Using the Countdown Timer / 使用倒计时器
From the main clock screen, click the "Countdown" button ("倒计时").
在主时钟界面，点击“倒计时”按钮。

Enter the desired hours, minutes, and seconds in the respective input fields. Click "Confirm" ("确认").
在相应的输入字段中输入所需的小时、分钟和秒数。点击“确认”。

The countdown will start on the next screen. Use the buttons to Start, Pause, Reset, or go back to Settings.
倒计时将在下一个屏幕上开始。使用按钮进行开始、暂停、重置或返回设置。

Project Structure / 项目结构
text
timer-app/
│
├── main.py                 # Application entry point / 应用程序入口点
├── MainPage.py            # Main clock display page / 主时钟显示页面
├── TimerPage.py           # Stopwatch (Count-up timer) page / 正计时器页面
├── CountDownTimeSetPage.py # Countdown timer setup page / 倒计时器设置页面
├── CountDownPage.py       # Countdown timer display page / 倒计时器显示页面
└── README.md              # This file / 本文件
How It Works / 实现原理
The application uses object-oriented programming with tkinter.Frame to create different pages (screens). The after() method is used to schedule periodic updates for the clocks and timers.

应用程序使用面向对象编程和 tkinter.Frame 来创建不同的页面（屏幕）。after() 方法用于调度时钟和计时器的定期更新。

Time Calculation: Functions like timer_rule() and out_put_format() handle the logic for incrementing/decrementing time and formatting it for display.
时间计算：timer_rule() 和 out_put_format() 等功能处理增加/减少时间并将其格式化为显示的逻辑。

Navigation: Each page is a class that destroys the current frame and creates an instance of the next one when navigating.
页面导航：每个页面都是一个类，在导航时会销毁当前框架并创建下一个页面的实例。
