from pypdf import PdfReader


def extract_text_from_file(
    file_path: str,
    content_type: str
) -> str:
    """
    Extract text from supported file types.
    """

    if content_type == "application/pdf":
        return extract_pdf_text(file_path)

    elif content_type in [
        "text/plain",
        "text/markdown"
    ]:
        return extract_text_file(file_path)

    raise ValueError(
        f"Unsupported content type: {content_type}"
    )


def extract_pdf_text(
    file_path: str
) -> str:
    reader = PdfReader(file_path)

    text_parts = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text_parts.append(page_text)

    return "\n".join(text_parts)


def extract_text_file(
    file_path: str
) -> str:
    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:
        return f.read()