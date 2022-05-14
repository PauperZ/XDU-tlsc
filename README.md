<h1 align="center">
    <img src="https://i.jpg.dog/file/jpg-dog/62d143823a1572e598c4e81403319a45.png" alt="XDU-tlsc" width="240">
</h1>
<p align="center">
XDU traffic light signal control system based on <a href="https://www.python.org/">Python</a>.
<p align="center">
  <a href="https://github.com/PauperZ/XDU-tlsc/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-brightgreen"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.6%2B-informational"></a>
</p>



## 一、设计方案

1. 红绿灯的时长控制和转换规则

   - 根据题目要求，南北走向的车流量是东西走向的两倍，考虑到车辆堆积问题，需对红绿灯时长进行合理控制。不妨设车辆直行、左转、右转比例一致，则南北车道包含两个直行车道，一个左转车道，直行绿灯时长应为左转时长的1/2。南北车道的车道数量和车流量均为东西车道两倍，考虑到东西车道右转和直行公用的车辆碰撞问题，直行和右转不能并行，故东西车道车辆更容易堆积，则东西绿灯时长为南北时长的3/2倍。设一次循环总时长为150s，则南北直行绿灯时长为20s，左转时长40s，右转绿灯常亮，红灯时长为90s；东西绿灯时长为90s，红灯时长为60s。
   - 转换规则参考大多数交通路口的红绿灯规则，循环自南北方向绿灯开始，先直行后左转，之后转红灯，右转绿灯常亮，东西方向红绿对应相反。

2. 输出展示方案

   采用 <a href="https://www.python.org/">Python</a> 语言的图像处理标准库 <a href="https://pillow.readthedocs.io/ ">Pillow</a> 制作 GIF 进行动画展示，并同时设置命令行展示方法，可以使用Python命令调用命令行进行红绿灯模拟演示。
   
   GIF动画展示效果：
   
   <h1 align="center">
       <img src="https://media.giphy.com/media/ghnrK5Wug2P9QzVnO8/giphy.gif" alt="XDU-tlsc" width="600">
   </h1>

 

## 二、测试方案

1. 将每一帧动画输入在 png_result 文件夹下，对每一帧动画进行检查，确保对应无误。

2. 分别使用 GIF 和 命令行方式进行展示，发现展示效果正常，红绿灯转换及时长控制均符合预期，对应无误。

   命令行展示效果截图：

   <h1 align="center">
       <img src="https://i.jpg.dog/file/jpg-dog/17365b45dd6d8c26a48ac3f5010e5d55.png" alt="XDU-tlsc" width="1080">
   </h1>

   
   

 

## 三、使用说明

1. 安装 Python 3 并勾选 Add Python to PATH 选项。

2. 使用 cmd 执行命令

   ~~~~
   pip install Pillow
   ~~~~

   安装运行环境依赖。

3. 在项目文件夹下使用 cmd 执行命令

   ~~~~
   Python main.py
   ~~~~

   生成 GIF 展示效果，并生成 png 文件，GIF 保存在项目根目录下， png文件保存在 png_result 文件夹下。

4. 在项目文件夹下使用 cmd 执行命令

   ~~~~
   Python cmdtest.py
   ~~~~

   启用命令行展示程序，该指令将在 cmd 窗口显示红绿灯转换效果。 

