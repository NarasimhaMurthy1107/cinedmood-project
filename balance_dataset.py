import os
import random

dataset_path = "dataset"
limit = 170

for mood in os.listdir(dataset_path):

    folder = os.path.join(dataset_path, mood)

    images = os.listdir(folder)

    if len(images) > limit:

        remove = random.sample(images, len(images) - limit)

        for img in remove:
            os.remove(os.path.join(folder, img))

print("Dataset Balanced Successfully")
