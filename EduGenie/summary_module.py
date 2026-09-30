from gemini_client import gemini_client


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Summarize the following text for a student.

Text:
{text}

Instructions:
- Identify the main ideas.
- Keep the summary clear and concise.
- Preserve important facts and concepts.
- Use simple student-friendly language.
- Do not add information that is not present in the original text.
- Use bullet points when useful.
"""

    return gemini_client.generate(prompt)