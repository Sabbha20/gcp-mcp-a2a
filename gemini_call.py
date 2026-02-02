from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me a joke about computers. In 1-2 lines"
)

print(response.text)