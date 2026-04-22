import os
import shutil

frame_folder = "frames"
dataset_folder = "dataset"

moods = ["Action","Comedy","Horror","Happy","Emotional"]

for mood in moods:
    os.makedirs(os.path.join(dataset_folder, mood.lower()), exist_ok=True)

for frame in os.listdir(frame_folder):

    for mood in moods:
        if frame.startswith(mood):

            src = os.path.join(frame_folder, frame)
            dst = os.path.join(dataset_folder, mood.lower(), frame)

            shutil.move(src, dst)

print("✅ Dataset organized successfully")