import os

from hello.main import main

if __name__ == "__main__":
    os.environ["LITELLM_USE_PROXY"]="true"
    os.environ["LITELLM_PROXY_URL"]="http://localhost:4000"
    os.environ["LITELLM_API_KEY"]="sk-1234"
    main() # does not work
