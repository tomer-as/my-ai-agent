import anthropic
import os

# משיכת המפתח שהגדרנו ב-Secrets של ה-Repository
api_key = os.getenv("ANTHROPIC_API_KEY")

def test_connection():
    if not api_key:
        return "Error: API Key not found! Check your Repository Secrets."
    
    client = anthropic.Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=50,
            messages=[{"role": "user", "content": "Hello! Are you connected and ready?"}]
        )
        return f"Claude response: {message.content[0].text}"
    except Exception as e:
        return f"Error connecting to Claude: {e}"

if __name__ == "__main__":
    print(test_connection())
