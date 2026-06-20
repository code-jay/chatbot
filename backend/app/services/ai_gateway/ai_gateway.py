from openai import OpenAI
import os
from app.core.config import settings

api_key=settings.OPENAI_API_KEY

client = OpenAI(api_key=api_key)


class AIGateway:
    def __init__(self):
        self.default_model = "gpt-4.1-mini"

    def build_input(self, system_prompt: str, messages: list):
        return [
            {
                "role": "system",
                "content": system_prompt
            },
            *messages
        ]

    def stream_response(self, input_messages, user_message: str):
        selected_model = self.choose_model(user_message)

        with client.responses.stream(
            model=selected_model,
            input=input_messages
        ) as stream:
            for event in stream:
                if event.type == "response.output_text.delta":
                    yield event.delta, selected_model


    def choose_model(self, message: str):
        message_lower = message.lower()

        if "code" in message_lower or "python" in message_lower:
            return "gpt-4.1"

        if "summarize" in message_lower:
            return "gpt-4.1-mini"

        return self.default_model