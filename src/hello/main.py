import dotenv
import litellm
import time
import os

def main():
    messages = [
            {"role": "system", "content": "Help if you can."},
            {
                "role": "user",
                "content": (
                    "What is your opinion of Colgate toothpastes and "
                    "can you tell me about health insurance plants? "
                ),
            },
        ]
    # os.environ["AWS_REGION"] = "ap-south-1" # "eu-west-1"
    params = { "aws_region_name": "ap-south-1" }
    params = { "aws_region_name": "eu-west-1" }
        
    start = time.monotonic()
    response = litellm.completion(
            model="bedrock/anthropic.claude-3-haiku-20240307-v1:0",
            messages=messages,
            tools={},
            tool_choice="auto",
            **params, 
        )
    end = time.monotonic()
    print(f"Response time: {end - start:.2f} seconds")
    print (response)
    response_message = response.choices[0].message
    print(f"Response message: {response_message.content}")
    

if __name__ == "__main__":
    
    main()
