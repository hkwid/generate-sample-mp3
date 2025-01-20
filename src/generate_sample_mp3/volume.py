from pydub import AudioSegment
from pydub.generators import Sine


def create_test_audio(volume_db=-10):
    sample_rate = 44100  # Set consistent sample rate

    # Create silence with specific sample rate
    silence = AudioSegment.silent(duration=1000, frame_rate=sample_rate)

    # Create tones with same sample rate
    left_tone = (
        Sine(440, sample_rate=sample_rate)
        .to_audio_segment(duration=1000)
        .apply_gain(volume_db)
    )
    right_tone = (
        Sine(440, sample_rate=sample_rate)
        .to_audio_segment(duration=1000)
        .apply_gain(volume_db)
    )

    # Create stereo channels with matched silence
    silent_segment = AudioSegment.silent(duration=1000, frame_rate=sample_rate)
    left_stereo = AudioSegment.from_mono_audiosegments(left_tone, silent_segment)
    right_stereo = AudioSegment.from_mono_audiosegments(silent_segment, right_tone)

    # Create pattern and repeat
    pattern = silence + left_stereo + right_stereo
    full_audio = pattern * 10

    # Export with dynamic filename
    filename = f"out/stereo_volume_{abs(volume_db)}db.mp3"  # Using abs() to remove minus sign  # Using abs() to remove minus sign
    full_audio.export(filename, format="mp3", parameters=["-ar", str(sample_rate)])
    print(f"Created: {filename}")


# Create MP3s with different volumes
create_test_audio(-20)  # Will create stereo_volume_20db.mp3
create_test_audio(-10)  # Will create stereo_volume_10db.mp3
create_test_audio(-5)  # Will create stereo_volume_5db.mp3
