import subprocess


def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully Converted")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")

convert_video_to_mp3("video.mp4","audio.mp3")