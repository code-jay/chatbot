def build_chat_prompt(
    previous_messages,
    rag_context: str
):
    messages = [
        {
            "role": "system",
            "content": f"""
You are a helpful assistant.

Use the document context below if it is relevant.
If the document context does not contain the answer, say that the uploaded document does not provide enough information.

Document Context:
{rag_context}
"""
        }
    ]

    messages += [
        {
            "role": msg.role,
            "content": msg.content
        }
        for msg in previous_messages
    ]

    return messages