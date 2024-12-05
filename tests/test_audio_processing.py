import numpy as np
import audio_processing

def test_process_audio():
    # Test with a simple input (a sine wave)
    test_data = np.array([0, 1, 0, -1, 0], dtype=np.int16)
    
    # Process the audio data
    processed_data = audio_processing.process_audio(test_data)
    
    # Check if the output is normalized
    assert np.max(np.abs(processed_data)) == 32767
