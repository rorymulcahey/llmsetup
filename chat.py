# chat.py

from llama_cpp import Llama

llm = Llama(model_path="mistral-7b-instruct-v0.2.Q4_K_M.gguf", n_ctx=2048, n_threads=8, verbose=False)

while True:
    prompt = input("You: ")
    print("Assistant:", llm(f"You are a helpful assistant.\nUser: {prompt}\nAssistant:", max_tokens=200, stop=["User:", "Assistant:"])["choices"][0]["text"].strip())
