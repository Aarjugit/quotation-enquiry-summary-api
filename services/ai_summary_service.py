from llm.gemini_client import GeminiClient


class AISummaryService:

    def __init__(self):
        self.gemini = GeminiClient()

    async def generate_summary(
        self,
        cleaned_data: dict
    ) -> dict:
        """
        Receives pre-sanitized enquiry and quotation data and passes
        it directly to Gemini for business summary generation.
        """
        # Send pre-cleaned data directly to Gemini
        summary = await self.gemini.summarize(
            cleaned_data
        )

        return summary


summary_service = AISummaryService()