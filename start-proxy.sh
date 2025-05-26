#!/usr/bin/env -S bash -x 

source ~/.local/.env-lite-llm-proxy

export AWS_ACCESS_KEY_ID=$(echo -n $(cat ~/.aws/credentials | grep aws_access_key_id | awk -F= '{ print $2}'))
export AWS_SECRET_ACCESS_KEY=$(echo $(cat ~/.aws/credentials | grep aws_secret_access_key | awk -F= '{ print $2}'))
export AWS_REGION=us-east-1

uv run litellm --debug --config config.yaml