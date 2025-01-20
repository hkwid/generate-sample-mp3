from pydub import AudioSegment
from pydub.generators import Sine


def create_test_audio():
    # Set consistent sample rate
    sample_rate = 44100

    # Create 1 second of silence
    silence = AudioSegment.silent(duration=1000, frame_rate=sample_rate)

    # Create 1 second of tone (440Hz) for left channel
    left_tone = Sine(440, sample_rate=sample_rate).to_audio_segment(duration=1000)
    silence_segment = AudioSegment.silent(duration=1000, frame_rate=sample_rate)
    left_stereo = AudioSegment.from_mono_audiosegments(left_tone, silence_segment)

    # Create 1 second of tone for right channel
    right_tone = Sine(440, sample_rate=sample_rate).to_audio_segment(duration=1000)
    right_stereo = AudioSegment.from_mono_audiosegments(silence_segment, right_tone)

    # Create the pattern: silence + left + right
    pattern = silence + left_stereo + right_stereo

    # Repeat the pattern for 30 seconds (10 times)
    full_audio = pattern * 10

    # Export as MP3
    full_audio.export("out/stereo_test_a.mp3", format="mp3")


if __name__ == "__main__":
    create_test_audio()
