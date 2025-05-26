import dotenv
import litellm
import time
import os
import os
from openai import OpenAI


def main():
    client = OpenAI(
        api_key="sk-1234",
        base_url="http://localhost:4000",
    )
    start = time.monotonic()    
    response = client.responses.create(
        model="claude-3-haiku-proxy",
        input = [
            {"role": "system", "content": "Help if you can."},
            {
                "role": "user",
                "content": (
                    "What is your opinion of Colgate toothpastes and "
                    "can you tell me about health insurance plants? "
                ),
            },
        ]
    )

    end = time.monotonic()
    print(f"Response time: {end - start:.2f} seconds")
    print (response)
    try:
        out = response.output[0].content[0].text
    except (AttributeError, IndexError, TypeError):
        out = None    
    print(f"Response message: {out}")
    

if __name__ == "__main__":
    
    main()
