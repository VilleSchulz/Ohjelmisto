import sounddevice as sd
import numpy as np
import pygame.mixer
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



