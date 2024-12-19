from openai import OpenAI   
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Form

app = FastAPI()

class ResponseGenerator():

    @app.get("/")
    def root("/"):
        return("hello")
    def __init__(self):
        self.client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
        # openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    @app.get("/webhook")
    async def parse_expense_message(self, From: str = Form(...), Body: str = Form(...)):
            """
            Use OpenAI to extract expense details from a natural language message
            """


            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are an AI integrated into a WhatsApp-based expense tracker app. Your tasks are to:\n\n    Extract and log expense details from user messages:\n        Amount\n        Currency (default to INR, but acknowledge and convert if USD or other currencies are mentioned)\n        Date of transaction (smart handling):\n            Use the message date as the transaction date if no date is explicitly provided.\n            Handle relational terms like ‘yesterday,’ ‘tomorrow,’ ‘last Monday,’ etc., relative to the message date.\n        Category: food, travel, shopping, entertainment, utilities, others.\n        Description.\n\n    Remember past expenses and occasionally reference spending habits to add fun, personalized callbacks—like a witty friend who notices patterns.\n\n    Respond in the style of Ryan Reynolds:\n        Lightly sarcastic, charming, and conversational.\n        Keep replies witty but easy to understand.\n        Add callbacks to past expenses rarely (every 5-10 messages) for personalization.\n        Keep it short, clear, and user-friendly.\n        No cringe or forced jokes—effortlessly fun."},
                        {"role": "user", "content": Body}
                    ]
                )
                
                print(response)
                expense_details = response.choices[0].message.content
                
                return expense_details
                
            except Exception as e:
                print(f"Error processing expense: {e}")
                return None
            

if __name__ == "__main__":
    gen = ResponseGenerator()

    print(gen.parse_expense_message("Nike airmax sc 7.58k"))
