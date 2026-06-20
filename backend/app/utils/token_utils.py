def count_words(text: str) -> int:
    return len((text or "").split())