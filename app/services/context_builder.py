from app.services.image_analyzer import analyze_image
from app.services.csv_analyzer import analyze_csv

def build_context(images: list[str], csvs: list[str]) -> str:
    context_parts = []

    for img in images:
        caption = analyze_image(img)
        context_parts.append(f"Image Insight: {caption}")

    for csv in csvs:
        stats = analyze_csv(csv)
        context_parts.append(f"CSV Insight:\n{stats}")

    return "\n\n".join(context_parts)
