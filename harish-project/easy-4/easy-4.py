import pyaudio
import wave

# Set up the audio format
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

# Set up the file to save the recording to
WAVE_OUTPUT_FILENAME = "output.wav"

# Create a PyAudio object
audio = pyaudio.PyAudio()

# Open a stream to record audio
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

# Create a list to store the recorded frames
frames = []

# Record audio until the user stops the program
while True:
    # Read a chunk of audio data from the stream
    data = stream.read(CHUNK)
    
    # Add the chunk to the list of frames
    frames.append(data)

    # Check if the user wants to stop recording
    if input("Press enter to stop recording..."):
        break

# Close the stream and PyAudio object
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
wave_file = wave.open(WAVE_OUTPUT_FILENAME, "wb")
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b"".join(frames))
wave_file.close()

print("Recording saved to", WAVE_OUTPUT_FILENAME)
