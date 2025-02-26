from pydub import AudioSegment
import os

def adjust_volume(input_dir, output_dir, volume_db):
    """
    Adjusts the volume of MP3 files in a directory by a specified amount (in dB).

    Args:
        input_dir: The directory containing the input MP3 files.
        output_dir: The directory to save the processed MP3 files.
        volume_db: The amount to adjust the volume by (in dB). Positive values increase volume, negative decrease.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp3"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)

            try:
                # Load the audio file
                audio = AudioSegment.from_mp3(input_file)

                # Adjust the volume
                audio = audio + volume_db  # volume_db is the gain (in dB)

                # Export the processed file
                audio.export(output_file, format="mp3")
                print(f"Processed: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Set the input and output directory paths
input_dir = r"C:\temp\audioprocess\input"
output_dir = r"C:\temp\audioprocess\output"

# Set the volume gain (in dB), +20 increases the volume by 20dB
volume_db = 20

# Call the function to process the audio files
adjust_volume(input_dir, output_dir, volume_db)
