import torch
import torchvision
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import torch.nn as nn

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

dataset = ImageFolder("dataset", transform=transform)

print("Classes:", dataset.classes)

loader = DataLoader(dataset, batch_size=16, shuffle=True)

model = torchvision.models.resnet18(pretrained=True)

model.fc = nn.Linear(model.fc.in_features, len(dataset.classes))

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

for epoch in range(5):

    total_loss = 0
    correct = 0
    total = 0

    for images, labels in loader:

        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        # Accuracy calculation
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    accuracy = 100 * correct / total

    print(f"Epoch {epoch+1} Loss: {total_loss:.2f} Accuracy: {accuracy:.2f}%")

torch.save(model.state_dict(),"models/mood_model.pth")

print(" Model Training Complete")