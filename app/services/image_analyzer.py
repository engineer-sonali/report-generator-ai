#images to text captions using BLIP model
from transformers import BlipProcessor, BlipForConditionalGeneration #for image captioning
from PIL import Image #to load images

#pretrained vision-language model from Hugging Face
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"   
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

def analyze_image(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=50)
    return processor.decode(output[0], skip_special_tokens=True)
