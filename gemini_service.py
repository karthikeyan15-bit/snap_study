import io
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image

from prompts import PROMPTS

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"


def _get_api_key():
    """Read the Gemini key from the environment or Streamlit secrets."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if api_key:
        return api_key.strip()

    try:
        api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
    except (FileNotFoundError, KeyError, AttributeError):
        api_key = None

    return api_key.strip() if isinstance(api_key, str) and api_key.strip() else None


def _get_client():
    """Create the Gemini client only when an analysis is requested."""
    api_key = _get_api_key()
    if not api_key:
        raise RuntimeError(
            "Gemini API key is not configured. "
            "For local development, add GEMINI_API_KEY=your-key to .env. "
            "For Streamlit Cloud, add GEMINI_API_KEY = \"your-key\" "
            "in the app's Settings > Secrets."
        )

    return genai.Client(api_key=api_key)


def analyze_image(image, mode="Explain"):
    prompt = PROMPTS.get(mode, PROMPTS["Explain"])

    # Convert Streamlit image input to PIL Image.
    if hasattr(image, "getvalue"):
        image = Image.open(io.BytesIO(image.getvalue()))
    elif hasattr(image, "read"):
        image = Image.open(io.BytesIO(image.read()))
    elif isinstance(image, bytes):
        image = Image.open(io.BytesIO(image))

    response = _get_client().models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image],
    )

    return response.text
