
from transformers import pipeline

class PromptGenerator:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')

    def generate_prompt(self, input_text: str, max_length: int = 50) -> str:
        prompts = self.generator(
            input_text,
            max_length=max_length,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
        )
        return prompts[0]['generated_text']
