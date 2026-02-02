from google.genai import Client, types
from dotenv import load_dotenv
import os

load_dotenv()

client = Client()

gconfigs = {
    # "contents":"Tell me a joke about computers.",
    "contents":"Tell me about first war of independence in India.",
    "model":"gemini-2.5-flash"
    }

# input_tokens = client.models.count_tokens(**gconfigs)
# print(f"Input tokens: {input_tokens.total_tokens}, \n {input_tokens}")

response = client.models.generate_content_stream(
    **gconfigs, 
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=300),
        # max_output_tokens=700,
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
            )
        ],
        system_instruction="You are expert in History and can provide detailed information on any historical event timelines."
        )
    )

# print(f"Response: {response.text}\n")
for chunks in response:
    print(chunks.text)
    
# print("\n\n\n")
# print(f"\nResponse tokens: {response.usage_metadata.total_token_count},\nCandidate tokens: {response.usage_metadata.candidates_token_count}\nThought tokens: {response.usage_metadata.thoughts_token_count}\nInput tokens: {response.usage_metadata.prompt_token_count} \n\nMetadata: {response.usage_metadata}")
