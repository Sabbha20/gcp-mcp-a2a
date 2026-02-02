from google.genai import Client, types
from dotenv import load_dotenv
import os

load_dotenv()

client = Client()

gconfigs = {"contents":"Tell me a joke about computers.",
"model":"gemini-2.5-flash"}

# input_tokens = client.models.count_tokens(**gconfigs)
# print(f"Input tokens: {input_tokens.total_tokens}, \n {input_tokens}")

response = client.models.generate_content(
    **gconfigs, 
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=300)
        )
    )

print(f"Response: {response.text}")
print(f"\nResponse tokens: {response.usage_metadata.total_token_count},\nCandidate tokens: {response.usage_metadata.candidates_token_count}\nThought tokens: {response.usage_metadata.thoughts_token_count}\nInput tokens: {response.usage_metadata.prompt_token_count} \n\n{response.usage_metadata}")
