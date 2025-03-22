from gpt4all import GPT4All
import time

# Model Initialization
start_time_model = time.time()
model = GPT4All(model_name='Llama-3.2-7B-Instruct-Q4_0.gguf')
end_time_model = time.time()
model_loading_time = end_time_model - start_time_model
print(f"\nModel loading time: {model_loading_time:.2f} seconds")

# Chat Session and Prompting
prompt1 = "Write a short story about a cat who goes on an adventure."

with model.chat_session():
    response1 = model.generate(prompt1)
    print(response1)

    prompt2 = "Continue the story, but make it funny."
    response2 = model.generate(prompt2)
    print(response2)