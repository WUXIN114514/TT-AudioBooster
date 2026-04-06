import pyaudio
import numpy as np
import tkinter as tk
from tkinter import ttk
import os
import urllib.request
import subprocess

def list_microphones():
    p = pyaudio.PyAudio()
    devices = []
    device_names = set()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_info['maxInputChannels'] > 0 and device_info['name'] not in device_names:
            devices.append((i, device_info['name']))
            device_names.add(device_info['name'])
    p.terminate()
    return devices

def check_voicemeeter():
    p = pyaudio.PyAudio()
    voicemeeter_found = False
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if 'VoiceMeeter Input' in device_info['name']:
            voicemeeter_found = True
            break
    p.terminate()
    return voicemeeter_found

def download_voicemeeter():
    url = "https://mksoftcdnhp.yesky.com/69d31d06/9fbb1cb012bf05b8fff11fa08978208a/uploadsoft/VoicemeeterProSetup-2.0.3.4.exe?fp=1cae639eb797ab970602c3b74bfc6e21"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    setup_path = os.path.join(desktop_path, "VoicemeeterProSetup.exe")
    
    print("正在下载VoiceMeeter Pro...")
    urllib.request.urlretrieve(url, setup_path)
    print(f"下载完成，文件保存到: {setup_path}")
    
    print("正在运行安装程序...")
    subprocess.run([setup_path], shell=True)
    return setup_path

def get_voicemeeter_output_index():
    p = pyaudio.PyAudio()
    output_index = None
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if 'VoiceMeeter Input' in device_info['name']:
            output_index = i
            break
    p.terminate()
    return output_index

def start_audio_processing(selected_device_index, gain=10):
    p = pyaudio.PyAudio()
    
    output_index = get_voicemeeter_output_index()
    
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=44100,
        input=True,
        input_device_index=selected_device_index,
        output=True,
        output_device_index=output_index,
        frames_per_buffer=1024
    )
    
    print(f"初始化成功，当前使用麦克风: {p.get_device_info_by_index(selected_device_index)['name']}")
    print(f"输出到: {p.get_device_info_by_index(output_index)['name']}")
    print("驱动正在运行")
    print("按 Ctrl+C 停止")
    
    try:
        while True:
            data = stream.read(1024)
            audio_data = np.frombuffer(data, dtype=np.float32)
            amplified_data = audio_data * gain
            amplified_data = np.clip(amplified_data, -1.0, 1.0)
            stream.write(amplified_data.tobytes())
    except KeyboardInterrupt:
        print("停止处理")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

def main():
    if not check_voicemeeter():
        print("未检测到虚拟设备通道设备")
        print("正在下载并安装VoiceMeeter")
        download_voicemeeter()
        print("请根据新窗口的指引进行安装并重启您的计算机")
        return
    
    voicemeeter_path = "C:\\Program Files (x86)\\VB\\Voicemeeter\\voicemeeterpro.exe"
    if os.path.exists(voicemeeter_path):
        print("正在打开VoiceMeeter Pro...")
        subprocess.Popen([voicemeeter_path])
    else:
        print("未找到VoiceMeeter Pro可执行文件")
    
    devices = list_microphones()
    
    if not devices:
        print("没有找到麦克风设备")
        return
    
    root = tk.Tk()
    root.title("最后一舞")
    root.geometry("550x450")
    
    label = ttk.Label(root, text="选择TT麦克风:")
    label.pack(pady=10)
    
    device_var = tk.StringVar()
    device_combobox = ttk.Combobox(root, textvariable=device_var, values=[name for _, name in devices])
    device_combobox.pack(pady=10)
    device_combobox.current(0)
    
    info_label = ttk.Label(root, text="使用说明:")
    info_label.pack(pady=10)
    
    info_text = ttk.Label(root, text="1. 选择TT使用的麦克风\n2. 原作者WuXin已经无力经营工作室 故开源此项目 项目永久免费\n3.此项目永久储存在github上 且原文件上传 当你没有看到这段提示的时候 你获取的已经是二改版本了", justify=tk.LEFT)
    info_text.pack(pady=10)
    
    def on_start():
        selected_name = device_var.get()
        selected_index = next(i for i, name in devices if name == selected_name)
        root.destroy()
        start_audio_processing(selected_index)
    
    start_button = ttk.Button(root, text="开始", command=on_start)
    start_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
