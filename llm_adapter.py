from llm_rewrite_openai import LlmRewriteOpenAI
import os


class LlmAdapter():
    def __init__(self, prompt, style):
        self.prompt = prompt
        self.style = style

    def __repr__(self):
        if "OPENAI_API_KEY" in os.environ:
            return LlmRewriteOpenAI(
                self.prompt,
                style=self.style,
                model_name=os.environ.get('OPENAI_MODEL', 'gpt-4.1-mini')
            ).run()
