from flask import Flask, request 
#from transformers import pipeline # First line



app = Flask(__name__)

#generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B') # Second line


# phrase = "The yellow monkey stole a while jeep in a market" # Third line



@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # try:
        #     req_data = request.json
        #     res = generator(req_data['phrase'], max_length=req_data['text_length'], do_sample=True, temperature=0.9) # Fourth line
        #     generated_text = res[0]['generated_text']
        #     return generated_text
        #     # print(req_data["templateName"])
        #     # return req_data["templateName"]
        # except:
        #     return False
        return "That's a get"
    elif request.method == 'GET':
        return "That is a GET request. Make a POST request instead"

        


if __name__ == "__main__":
    app.run(host='0.0.0.0')

    