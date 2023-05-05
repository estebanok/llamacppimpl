# llamacppAPI Implementation
This is made to an alternative to OpenAI API

This will run a Uvicorn Web Server to make requests to Llama model

You will need the vicuna or llama model, I'm using it from huggingface.co https://huggingface.co/eachadea/ggml-vicuna-7b-1.1

You will need to install via pip the next modules

uvicorn[standard] fastapi llama-cpp-python

first you need to run the api via PS or CMD

uvicorn llamaapi:app --port 8002

in another terminal you can consume it or use it in your application

in my case im making a prompt in a python file so I use:

python .\llamaclient.py

Cheers.
