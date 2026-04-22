import cv2
import os

video_folder = "videos"
frame_folder = "frames"

os.makedirs(frame_folder, exist_ok=True)

for video in os.listdir(video_folder):

    video_path = os.path.join(video_folder, video)

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps)

    count = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % interval == 0:
            name = video.split(".")[0] + "_" + str(saved) + ".jpg"
            cv2.imwrite(os.path.join(frame_folder, name), frame)
            saved += 1

        count += 1

    cap.release()

print("✅ All frames extracted")