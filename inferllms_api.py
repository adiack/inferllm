import json
import requests
import sys

FLAN_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
BLENDER_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
BLOOM_API_URL  = "https://api-inference.huggingface.co/models/bigscience/bloom"
BERT_API_URL  = "https://api-inference.huggingface.co/models/bert-base-uncased"
BLOOM_PETAL_API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom-petals"
GPTJ6B_API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B"
GPT2_API_URL = "https://api-inference.huggingface.co/models/gpt2"
FASTSPEECH_API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"

headers = {"Authorization": "Bearer [your key]"}
inputs= "What did the ant eat the ball?"
inputs=sys.argv[1]
print("\nPrompt: "+inputs)
def query(payload):
	response = requests.post(GPT2_API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": inputs,
})
out=output[0]
print("\n\nGPT2\n")
print(out["generated_text"])


def query(payload):
	response = requests.post(BLOOM_API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": inputs,
})
out=output[0]
print("\n\nBLOOM\n")
print(out["generated_text"])

def query(payload):
	response = requests.post(GPTJ6B_API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": inputs,
})
print("\n\nGPTJ6B\n")
out=output[0]
print(out["generated_text"])



def query(payload):
	response = requests.post(FLAN_API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": inputs,
})
print("\n\nFLAN-T5-XL\n")
out=output[0]
print(out["generated_text"])
