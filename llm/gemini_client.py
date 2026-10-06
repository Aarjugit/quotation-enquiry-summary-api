import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts.summary_prompt import SUMMARY_PROMPT


load_dotenv()


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")
        model = os.getenv("GEMINI_MODEL")

        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not configured")

        if not model:
            raise RuntimeError("GEMINI_MODEL is not configured")

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = model

    async def summarize(self, data: dict) -> dict:

        json_data = json.dumps(
            data,
            ensure_ascii=False
        )

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=json_data,
            config=types.GenerateContentConfig(
                system_instruction=SUMMARY_PROMPT,
                temperature=0.2,
                response_mime_type="application/json"
            )
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response"
            )

        try:

            return json.loads(response.text)

        except json.JSONDecodeError as exc:

            raise RuntimeError(
                f"Gemini returned invalid JSON: {response.text}"
            ) from exc