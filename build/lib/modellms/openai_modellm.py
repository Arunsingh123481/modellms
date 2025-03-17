import openai

class OpenAIModel:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("OpenAI API key required")
        self.client = openai.OpenAI(api_key=api_key)

    def query(self, prompt, model="gpt-3.5-turbo"):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"OpenAI Error: {str(e)}"