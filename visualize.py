import numpy as np
import matplotlib.pyplot as plt

def plot_waveform(audio_data):
    """
    Visualize the waveform of the audio data in real time.
    
    Args:
    - audio_data: Processed audio data as a numpy array.
    """
    plt.clf()  # Clear the previous plot
    plt.plot(audio_data)
    plt.title("Real-Time Audio Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.pause(0.01)  # Pause for a brief moment to update the plot
