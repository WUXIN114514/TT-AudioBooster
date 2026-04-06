# 使用说明

这是一段简短的使用说明

## 前提
安装VoiceMeeter Banana  （如果电脑没有程序会自动安装 Q群内发布的压缩包中自带）

## 使用方法

### 对于 编译好的程序:最后一舞.exe

1. 选择麦克风
2. 打开VoiceMeeter Banana
3. 点击右上角 Menu - Load Setting... - 选择文件夹中带出的XML文件 驱动配置（请勿胡乱修改）.xml  - 确定 -配置成功加载
4. 在驱动内点击开始 出现

   ```
   初始化成功，当前使用麦克风: ***
   输出到: VoiceMeeter Input (VB-Audio Voi
   驱动正在运行
   按 Ctrl+C 停止
   ```

   为成功运行状态

5. 在TT内选择麦克风设备为VoiceMeeter Output

6. 开始使用

### 对于 未编译好的原始py文件:最后一舞.py

安装开发版本 python 3.8.9 并配置好PATH

#### 所需库
- pyaudio
- numpy
- tkinter
- ttk
- os
- urllib.request -------下载VoiceMeeter Banana
- subprocess

在cmd / 其他控制台 运行 python mic_volume_booster.py

出现软件本体即为开始运行

使用教程参考上文[对于 编译好的程序:最后一舞.exe]


打包成exe的指令请自行搜索 此教程不做赘述


此项目作者为无心 项目较为简短 目前还有一个c++版本未发布 此版本功能更全面 但是我已经无心制作这个版本了 我会发布现有的制作好的cpp文件 BUG较多 其他的由你们自行修复 感谢使用

软件没有杀毒报告（因为源代码已经开源）如果不放心编译好的软件可以自行阅读代码之后调试运行
