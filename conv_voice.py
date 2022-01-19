from pydub import AudioSegment
import os


def convert(file_name, message_id, user_id):
    voice = AudioSegment.from_file(file_name)
    voice = voice.set_frame_rate(16000)
    voice.export(f"data/{user_id}/audio_message_{message_id}.wav", format='wav')
    delite_file(file_name)
    

def delite_file(file):
    os.remove(file)