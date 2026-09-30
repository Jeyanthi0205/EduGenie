from gemini_client import gemini_client


def explain_topic(topic: str) -> str:
    """
    Explain a topic in simple, student-friendly language.
    """

    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic to a student who is learning it for the first time.

Topic:
{topic}

Instructions:
- Start with a simple definition.
- Explain the concept step by step.
- Use a simple real-world example.
- Mention important points the student should remember.
- Avoid unnecessarily complicated terminology.
- Use headings or bullet points when useful.
- Make the explanation educational and easy to revise.
"""

    return gemini_client.generate(prompt)