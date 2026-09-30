import time

from google import genai

from config import settings


class GeminiClient:
    """Reusable Gemini client with retry handling."""

    def __init__(self):
        if not settings.gemini_api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is missing. Add it to the .env file."
            )

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = settings.gemini_model

    def generate(
        self,
        prompt: str,
        max_retries: int = 5,
    ) -> str:
        """Generate text from Gemini with retry handling."""

        last_error = None

        for attempt in range(1, max_retries + 1):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                )

                if not response.text:
                    raise RuntimeError(
                        "Gemini returned an empty response."
                    )

                return response.text.strip()

            except Exception as error:
                last_error = error

                error_text = str(error)

                print(
                    f"Gemini request failed "
                    f"(attempt {attempt}/{max_retries}): {error}"
                )

                # Do not retry quota errors.
                if (
                    "429" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                ):
                    raise RuntimeError(
                        "Gemini API quota exceeded. "
                        "Please wait for the quota to reset or check "
                        "your Gemini API usage and billing settings."
                    ) from error

                if attempt < max_retries:
                    wait_time = min(
                        5 * (2 ** (attempt - 1)),
                        30,
                    )

                    print(
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

        raise RuntimeError(
            f"Gemini request failed after "
            f"{max_retries} attempts: {last_error}"
        )


gemini_client = GeminiClient()