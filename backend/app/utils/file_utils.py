def sanitize_filename(filename: str) -> str:
    return (filename or "uploaded_file").replace(" ", "_")