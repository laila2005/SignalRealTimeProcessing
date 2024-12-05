# microphone_setup.py

import pyaudio

def get_microphone_device():
    p = pyaudio.PyAudio()
    device_index = None
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if 'RDP' in device_info['name']:  # Adjust as necessary
            device_index = i
            break
    return device_index
