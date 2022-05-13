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

 

## 二、测试方案

1. ...
2. ...

 

## 三、使用说明

1. ...
2. ...
