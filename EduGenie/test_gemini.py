from dotenv import load_dotenv
from google import genai
import os
import time

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY was not found.")

if not model:
    raise RuntimeError("GEMINI_MODEL was not found.")

print("API key found: YES")
print(f"Model from .env: {model}")

client = genai.Client(api_key=api_key)

for attempt in range(1, 4):
    print(f"\nAttempt {attempt}/3...")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Answer in one short sentence: What is the largest ocean in the world?",
        )

        print("\nSUCCESS!")
        print("Gemini response:")
        print(response.text)
        break

    except Exception as error:
        print(f"Attempt {attempt} failed.")
        print(f"Error: {error}")

        if attempt < 3:
            print("Waiting 5 seconds before retry...")
            time.sleep(5)
        else:
            print("\nAll attempts failed.")
            raise