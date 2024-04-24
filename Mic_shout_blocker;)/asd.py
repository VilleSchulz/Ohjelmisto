import sounddevice as sd
import numpy as np
import pygame.mixer
import tkinter as tk
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('apina.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for sound to finish playing
        pygame.time.Clock().tick(10)  # Check every 10 milliseconds
    pygame.mixer.music.stop()  # Stop the sound
    pygame.mixer.quit()  # Quit the mixer module

def print_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(f'Microphone Volume: {volume_norm:.2f}')
    if volume_norm > 20:
        play_sound()

    return volume_norm
while True:
    with sd.InputStream(callback=print_volume):
        sd.sleep(1000)



"""import sounddevice as sd
import numpy as np
import pygame.mixer
import tkinter as tk

threshold = 25

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('apina.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for sound to finish playing
        pygame.time.Clock().tick(10)  # Check every 10 milliseconds
    pygame.mixer.music.stop()  # Stop the sound
    pygame.mixer.quit()  # Quit the mixer module

def set_threshold(value):
    global threshold
    threshold = value

def print_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print(f'Microphone Volume: {volume_norm:.2f}')
    if volume_norm > threshold:
        play_sound()

# Create the main window
root = tk.Tk()
root.title("Oo jo hilijaa")

# Create a label
label = tk.Label(root, text="Liikutaha sitä slaikkaria\n"
                            "niin muija ei kidise!:")
label.pack()

# Create a slider
slider = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL, command=set_threshold)
slider.set(threshold)
slider.pack()

# Start the audio stream
with sd.InputStream(callback=print_volume):
    # Run the main event loop
    root.mainloop()"""