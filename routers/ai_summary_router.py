from fastapi import APIRouter, HTTPException

from schemas.ai_summary_schema import AISummaryRequest
from services.ai_summary_service import summary_service
from services.data_sanitizer import sanitize_data


router = APIRouter(
    prefix="/api/ai",
    tags=["AI Summary"]
)


@router.post("/summary")
async def generate_ai_summary(
    request: AISummaryRequest
):
    """
    Sanitizes raw frontend enquiry and quotation data,
    then passes the cleaned data to Gemini for summary generation.
    """

    try:
        # Get original frontend JSON
        raw_data = request.model_dump()

        # Sanitize inside the same pipeline
        cleaned_data = sanitize_data(raw_data)

        # Send cleaned data to Gemini
        summary = await summary_service.generate_summary(
            cleaned_data
        )

        return {
            "success": True,
            "summary": summary
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"AI summary generation failed: {str(exc)}"
        )