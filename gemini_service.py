import os
import io
from PIL import Image
from google import genai
from dotenv import load_dotenv

from prompts import PROMPTS

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3.5-flash-lite"


def analyze_image(image, mode="Explain"):
    prompt = PROMPTS.get(mode, PROMPTS["Explain"])

    # Convert Streamlit image input to PIL Image
    if hasattr(image, 'read'):
        image_bytes = image.read()
        image = Image.open(io.BytesIO(image_bytes))
    elif hasattr(image, 'getvalue'):
        image_bytes = image.getvalue()
        image = Image.open(io.BytesIO(image_bytes))
    elif isinstance(image, bytes):
        image = Image.open(io.BytesIO(image))

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[
            prompt,
            image
        ]
    )

    return response.text