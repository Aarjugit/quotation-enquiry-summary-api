# AI Enquiry & Quotation Summary API

FastAPI-based backend service that receives enquiry and quotation data from an Admin Dashboard, sanitizes sensitive information, sends the cleaned data to Google Gemini, and returns a structured business summary suitable for displaying in an Angular dashboard popup.

---

## Overview

The system is designed to summarize:

- Multiple enquiries
- Enquiry status
- Customer/company information
- Expected budget
- Expected timeline
- Feedback
- Follow-ups
- Multiple quotations per enquiry
- Quotation status
- Quotation amount
- Quotation items
- GST/taxes
- Payment terms
- Delivery
- Installation
- Freight
- Validity
- Warranty
- Recommended administrator action

The frontend sends the **original JSON only once**.

The backend handles sanitization internally before sending information to Gemini.

---

## Architecture

```text
Angular Admin Dashboard
        |
        | POST /api/ai/summary
        | Original JSON
        v
+---------------------------+
| FastAPI Router             |
| ai_summary_router.py       |
+---------------------------+
        |
        v
+---------------------------+
| Data Sanitizer             |
| data_sanitizer.py         |
+---------------------------+
        |
        | Clean JSON
        v
+---------------------------+
| AI Summary Service         |
| ai_summary_service.py     |
+---------------------------+
        |
        v
+---------------------------+
| Gemini Client              |
| gemini_client.py           |
+---------------------------+
        |
        | Prompt + Clean JSON
        v
+---------------------------+
| Google Gemini              |
+---------------------------+
        |
        | Structured JSON
        v
FastAPI
        |
        v
Angular Dashboard
        |
        v
AI Summary Popup
