from transformers import TFAutoModelForCausalLM, AutoTokenizer

# Load pre-trained model and tokenizer
model = TFAutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Encode a prompt to get input_ids
prompt = "Hello, I am"
input_ids = tokenizer.encode(prompt, return_tensors="tf")

# Generate text
output = model.generate(input_ids, max_length=100, num_return_sequences=1, 
                         no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
