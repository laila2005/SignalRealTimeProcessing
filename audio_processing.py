# audio_processing.py

import pyaudio

# audio_processing.py
def process_audio(audio_data):
    # Example processing logic: just return the raw data for now
    return audio_data

def record_audio(device_index):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=1024)

    print("Recording...")
    frames = []
    try:
        for _ in range(0, int(44100 / 1024 * 5)):  # 5 seconds of audio
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass
    finally:
        print("Recording finished")
        stream.stop_stream()
        stream.close()
        p.terminate()
