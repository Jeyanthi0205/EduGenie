from gemini_client import gemini_client


prompt = """
You are EduGenie, an educational AI assistant.

Answer this question in a simple way suitable for a student:

What is the largest ocean in the world?
"""

answer = gemini_client.generate(prompt)

print("Gemini client test successful!")
print()
print("Answer:")
print(answer)