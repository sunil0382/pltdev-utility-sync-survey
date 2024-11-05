from datetime import datetime


def ensure_iso_format(date_str):
    try:
        # Try to parse it to ensure it's a valid datetime string
        datetime.fromisoformat(date_str)
        return date_str  # Already in ISO format
    except ValueError:
        # If parsing fails, attempt other formats (if needed)
        print(f"Invalid or unexpected date format: {date_str}")
        return None  # Or handle it as appropriate
