import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from config import WHISPER_DEPLOYMENT
from client import client
from pydub import AudioSegment
import math
import eyed3

MAX_SIZE_MB = 25

def calculate_segment_duration_and_num_segments(duration_seconds, overlap_seconds, max_size, bitrate_kbps):
    """Calculate the duration and number of segments for an audio file."""
    seconds_for_max_size = (max_size * 8 * 1024) / bitrate_kbps
    num_segments = max(2, int(duration_seconds / seconds_for_max_size) + 1)
    total_overlap = (num_segments - 1) * overlap_seconds
    actual_playable_duration = (duration_seconds - total_overlap) / num_segments
    return num_segments, actual_playable_duration + overlap_seconds

def construct_file_names(path_to_mp3, num_segments):
    """Construct new file names for the segments of an audio file."""
    directory = os.path.dirname(path_to_mp3)
    base_name = os.path.splitext(os.path.basename(path_to_mp3))[0]
    padding = max(1, int(math.ceil(math.log10(num_segments))))
    new_names = [os.path.join(directory, f"{base_name}_{str(i).zfill(padding)}.mp3") for i in range(1, num_segments + 1)]
    return new_names

def convert_to_mp3(original_path, target_format="mp3"):
    """Convert an audio file to MP3 format."""
    audio = AudioSegment.from_file(original_path)
    mp3_path = original_path.rsplit(".", 1)[0] + "." + target_format
    audio.export(mp3_path, format=target_format)
    return mp3_path

def split_mp3(path_to_audio, overlap_seconds, max_size=MAX_SIZE_MB):
    """First convert to mp3 and then split into segments if still > 25mb (API file size limit)."""
    if not os.path.exists(path_to_audio):
        raise ValueError(f"File {path_to_audio} does not exist.")
    if not path_to_audio.endswith(".mp3"):        
        path_to_audio = convert_to_mp3(path_to_audio)
    audio_file = eyed3.load(path_to_audio)
    if audio_file is None:
        raise ValueError(f"File {path_to_audio} is not a valid mp3 file.")
    duration_seconds = audio_file.info.time_secs
    bitrate_kbps = audio_file.info.bit_rate[1]
    file_size_MB = os.path.getsize(path_to_audio) / (1024 * 1024)
    if file_size_MB < max_size:        
        return [path_to_audio]
    num_segments, segment_duration = calculate_segment_duration_and_num_segments(duration_seconds, overlap_seconds, max_size, bitrate_kbps)
    new_file_names = construct_file_names(path_to_audio, num_segments)
    original_audio = AudioSegment.from_mp3(path_to_audio)
    start = 0
    for i in range(num_segments):
        if i == num_segments - 1:
            segment = original_audio[start:]
        else:
            end = start + segment_duration * 1000
            segment = original_audio[start:int(end)]
        segment.export(new_file_names[i], format="mp3")
        start += (segment_duration - overlap_seconds) * 1000
    os.remove(path_to_audio)
    return new_file_names

def get_transcription(audio_file_path):    
    model = 'whisper-1'
    if WHISPER_DEPLOYMENT != '':
        model = WHISPER_DEPLOYMENT
    allowed_file_types = ['.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav', '.webm']
    file_extension = os.path.splitext(audio_file_path)[1]
    if file_extension.lower() not in allowed_file_types:
        raise ValueError("Invalid file type. Supported file types are: mp3, mp4, mpeg, mpga, m4a, wav, and webm")    
    max_file_size = MAX_SIZE_MB * 1024 * 1024
    if os.path.getsize(audio_file_path) > max_file_size:
        chunk_paths = split_mp3(audio_file_path, 1)
        transcripts = []
        if len(chunk_paths) == 1:
            chunk_path = chunk_paths[0]
            with open(chunk_path, 'rb') as chunk_obj:
                transcript_single = client.audio.transcriptions.create(model=model, file=chunk_obj)
            os.remove(chunk_path)
            return transcript_single.text
        else:
            print(f"{audio_file_path.split('/')[-1]} has been split into chunks for processing.")
            for chunk_path in chunk_paths:                
                with open(chunk_path, 'rb') as file_obj:
                    transcript = client.audio.transcriptions.create(model=model, file=file_obj)
                    transcripts.append(transcript.text)
                os.remove(chunk_path)
            return "\n***********\n".join(transcripts)    
    # Open the file in binary mode and pass the file object to the API
    with open(audio_file_path, 'rb') as file_obj:
        transcript = client.audio.transcriptions.create(model=model, file=file_obj)
    return transcript.text