import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

model, preprocess = clip.load("ViT-B/32", device=device)

def get_image_features(image):
    image = preprocess(image).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model.encode_image(image)
    return features

def classify_outfit(image):
    labels = [
        "casual outfit",
        "formal outfit",
        "party outfit",
        "sporty outfit",
        "stylish outfit",
        "bad outfit"
    ]

    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = clip.tokenize(labels).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

        similarity = (image_features @ text_features.T).softmax(dim=-1)

    return {labels[i]: float(similarity[0][i]) for i in range(len(labels))}