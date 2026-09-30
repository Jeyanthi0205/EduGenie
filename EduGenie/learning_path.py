from gemini_client import gemini_client


def generate_learning_path(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Create a personalized learning path for a student who wants to learn:

Topic:
{topic}

Requirements:
- Start from beginner level.
- Progress gradually toward advanced concepts.
- Organize the learning path into clear stages.
- Give each stage a difficulty level.
- Explain what the student should learn at each stage.
- Suggest useful learning resources or resource types.
- Include practical exercises or projects where appropriate.
- Keep the plan realistic and easy to follow.
- Use simple student-friendly language.
- Do not assume the student already has advanced knowledge.

Return the learning path using clear headings and bullet points.
"""

    return gemini_client.generate(prompt)