from google.genai import Client
from dotenv import load_dotenv

load_dotenv()

client = Client()

gconfigs = {
    "contents":"Create an image of jacksparrow riding a dragon",
    "model":"gemini-2.5-flash-image"
    }

response = client.models.generate_content(**gconfigs)

for parts in response.parts:
    if parts.text is not None:
        print(parts.text)
    elif parts.inline_data is not None:
        img = parts.as_image()
        img.save("imgs/jacksparrow_dragon1.png")
        print("Image generated")