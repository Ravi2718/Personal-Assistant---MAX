import sys
import os
from playsound import playsound

# Function to handle resource paths, especially for bundled files
def resource_path(relative_path):
    try:
        # When running as an executable, PyInstaller sets _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # For regular Python script (not as .exe)
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Paths to the audio files (using resource_path to handle packaging)
activation_sound_path = resource_path("Voicy_Siri sound effect.mp3")
end_sound_path = resource_path("end_sound.mp3")
sound_path = resource_path("sound.mp3")

# Function to play the activation sound
def play_activation_sound():
    print("Playing activation sound...")
    playsound(activation_sound_path)

# Function to play the end sound
def play_end_sound():
    print("Playing end sound...")
    playsound(end_sound_path)

# Main function to simulate assistant behavior
def assistant():
    print("Assistant is ready.")
    play_activation_sound()  # Play the activation sound
    
    # Simulate assistant's work (this is where you can add functionality like voice commands)
    print("Processing command...")  # You can replace this with actual voice recognition
    play_end_sound()  # Play the end sound after processing the command
    print("Assistant is done.")

# Run the assistant
if __name__ == "__main__":
    assistant()
