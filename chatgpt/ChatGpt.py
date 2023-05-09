from config import OPENAI_API_KEY
import openai
class ChatGpt:
    def __init__(self) -> None:
        openai.api_key = OPENAI_API_KEY

    def ask_gpt(self, message: str) -> str:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{message}"}
            ]
        )
        return completion.get("choices")[0].message.content