def safe_title(text: str, max_length: int = 40) -> str:
    text = (text or "").strip()
    return text[:max_length] if text else "New Conversation"