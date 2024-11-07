import os
import time
from plyer import notification
from playsound import playsound

def notify_user(file_name):
    notification.notify(
        title="File Received",
        message=f"You have received a file: {file_name}",
        timeout=10
    )

def play_audio(audio_file):
    playsound(audio_file)

def monitor_directory(directory, audio_file):
    already_seen = set(os.listdir(directory))
    while True:
        time.sleep(1)
        current_files = set(os.listdir(directory))
        new_files = current_files - already_seen
        if new_files:
            for file_name in new_files:
                notify_user(file_name)
                play_audio(audio_file)
            already_seen = current_files

if __name__ == "__main__":
    directory_to_monitor = "path/to/your/director"
    audio_file_path = "c:\Users\DELL\Documents\WhatsApp Audio 2024-11-06 at 10.35.37 PM.ogg"
    monitor_directory(directory_to_monitor, audio_file_path)
