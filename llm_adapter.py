from llm_rewrite_openai import LlmRewriteOpenAI
import os
import redis


class LlmAdapter():
    def __init__(self, prompt, style):
        self.prompt = prompt
        self.style = style
        self.redis_client = redis.Redis(host='redis', port=6379, db=0)

    def _llm_call(self):    
        if "OPENAI_API_KEY" in os.environ:
            return LlmRewriteOpenAI(
                self.prompt,
                style=self.style,
                model_name="gpt-4.1-mini"
            ).run()

    def _cache_response(self):
        cache_key = f'langchain_{self.style}_{self.prompt[:128]}'
        cached_response = self.redis_client.get(cache_key)
        if cached_response:
            return cached_response.decode('utf-8')

        response = self._llm_call()
        self.redis_client.set(cache_key, response)
        return response
    
    def __repr__(self):
        return self._cache_response()
