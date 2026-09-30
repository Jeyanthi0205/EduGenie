import json

from gemini_client import gemini_client
from schemas import QuizResponse


def generate_quiz(topic: str) -> QuizResponse:
    """
    Generate exactly 3 MCQs with exactly 4 options each.
    """

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create a quiz for the following topic:

Topic:
{topic}

Requirements:
- Generate exactly 3 multiple-choice questions.
- Each question must have exactly 4 options.
- Only one option must be correct.
- Include the correct answer.
- Include a short explanation for the correct answer.
- Keep the questions appropriate for students.
- Return ONLY valid JSON.
- Do not use Markdown.
- Do not add text before or after the JSON.

Return exactly this structure:

{{
  "topic": "{topic}",
  "questions": [
    {{
      "question": "Question text",
      "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      "answer": "Correct option",
      "explanation": "Why this answer is correct"
    }}
  ]
}}
"""

    raw_response = gemini_client.generate(prompt)

    cleaned = raw_response.strip()

    # Remove accidental Markdown code fences.
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()

        if lines and lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        cleaned = "\n".join(lines).strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"Gemini returned invalid quiz JSON: {error}"
        ) from error

    try:
        quiz = QuizResponse.model_validate(data)
    except Exception as error:
        raise RuntimeError(
            f"Quiz data validation failed: {error}"
        ) from error

    # Additional validation.
    if len(quiz.questions) != 3:
        raise RuntimeError(
            "Quiz must contain exactly 3 questions."
        )

    for index, question in enumerate(quiz.questions, start=1):
        if len(question.options) != 4:
            raise RuntimeError(
                f"Question {index} must have exactly 4 options."
            )

        if question.answer not in question.options:
            raise RuntimeError(
                f"Question {index} has an answer "
                "that is not one of its options."
            )

    return quiz