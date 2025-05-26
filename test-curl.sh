#!/usr/bin/env -S bash -x 


curl --location 'http://0.0.0.0:4000/v1/models' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json'




curl --location 'http://0.0.0.0:4000/chat/completions' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "claude-3-haiku-proxy",
    "messages": [
        {
        "role": "user",
        "content": "what llm are you"
        }
    ]
}'
