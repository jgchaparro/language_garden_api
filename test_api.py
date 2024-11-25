from fastapi import FastAPI
from llama_cpp import Llama
import os

# Load model
# llm = Llama(model_path = os.path.join('models', "language_garden-ell-tsd-8b.Q5_K_M.gguf"))
llm = Llama.from_pretrained(
	repo_id="jgchaparro/language_garden-ell-tsd-8B-GGUF",
	filename="language_garden-ell-tsd-8b.Q5_K_M.gguf",
)

app = FastAPI()

@app.get("/translate/")
async def root(text: str):
    response = llm.create_chat_completion(
        messages = [
            {
                "role": "user",
                "content": f"Translate from Greek to Tsakonian: {text}"
            }
        ],
        temperature = 0,
    )
    translation = response['choices'][0]['message']['content'].replace(f'Translation to Tsakonian: ', '')
    return {"translation": translation}