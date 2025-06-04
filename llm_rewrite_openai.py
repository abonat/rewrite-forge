from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI


class LlmRewriteOpenAI():
    def __init__(self, content, style, model_name):
        self.chain = LLMChain(
            llm=ChatOpenAI(model_name=model_name, temperature=.95),
            prompt=PromptTemplate(
                template="\n".join([
                    "Question: {question}",
                    f"Please, rewrite the text to sounds like {style}",
                    "Answer:"
                ]),
                input_variables=["question"]
            )
        )
        self.question = "\n".join([
            "Please, rewrite the following content:",
            content
        ])
    def run(self):
        try:
            return self.chain.run(self.question)
        except Exception as e:
            print(f"An error occurred: {e}")
