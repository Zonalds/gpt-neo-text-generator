import sys

from transformers import pipeline # First line

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B') # Second line

# phrase = "The yellow monkey stole a while jeep in a market" # Third line


#argv[1] is phrase, argv[2] is max_length
res = generator(sys.argv[1], sys.argv[1], do_sample=True, temperature=0.9) # Fourth line
generated_text = res[0]['generated_text']
print(generated_text)