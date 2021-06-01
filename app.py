from flask import Flask, request 




app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # try:
        #     req_data = request.json
        #     
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

    