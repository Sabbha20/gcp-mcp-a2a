from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

gconfigs = {"contents":"Tell me a joke about computers. In 1-2 lines",
"model":"gemini-2.5-flash"}

input_tokens = client.models.count_tokens(**gconfigs)
print(f"Input tokens: {input_tokens.total_tokens}, \n {input_tokens}")

response = client.models.generate_content(**gconfigs)

print(f"Response: {response.text}")
print(f"\nResponse tokens: {response.usage_metadata.total_token_count}, \n{response.usage_metadata}")
