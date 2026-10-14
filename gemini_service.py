import io
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image

from prompts import PROMPTS

load_dotenv()

MODEL_NAME = "gemini-3.5-flash-lite"


@st.cache_resource
def get_client():
    """Create and reuse the Gemini API client."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get(
                "GOOGLE_API_KEY"
            )
        except (AttributeError, FileNotFoundError, KeyError):
            api_key = None

    if not isinstance(api_key, str) or not api_key.strip():
        raise RuntimeError(
            "Gemini API key is not configured. "
            "For local development, add GEMINI_API_KEY=your-key to .env. "
            "For Streamlit Cloud, add GEMINI_API_KEY = \"your-key\" "
            "in the app's Settings > Secrets."
        )

    return genai.Client(api_key=api_key.strip())


def analyze_image(image, mode="Explain"):
    prompt = PROMPTS.get(mode, PROMPTS["Explain"])

    # Convert Streamlit image input to PIL Image.
    if isinstance(image, bytes):
        image = Image.open(io.BytesIO(image))
    elif hasattr(image, "getvalue"):
        image = Image.open(io.BytesIO(image.getvalue()))
    elif hasattr(image, "read"):
        image = Image.open(io.BytesIO(image.read()))

    image = image.convert("RGB")

    client = get_client()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image],
    )

    return response.text
