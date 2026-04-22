import torch
import torchvision
from torchvision import transforms
from PIL import Image
import os
from collections import Counter

classes = ['action','comedy','emotional','happy','horror']

model = torchvision.models.resnet18()
model.fc = torch.nn.Linear(model.fc.in_features, len(classes))
model.load_state_dict(torch.load("models/mood_model.pth"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

frame_folder = "frames"

predictions = []

for frame in os.listdir(frame_folder):

    img = Image.open(os.path.join(frame_folder, frame))

    img = transform(img).unsqueeze(0)

    output = model(img)

    _, pred = torch.max(output,1)

    predictions.append(classes[pred.item()])

final_mood = Counter(predictions).most_common(1)[0][0]

print("🎬 Final Scene Mood:", final_mood)