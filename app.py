from flask import Flask, render_template, request
import requests, json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    headers = {'Authorization': 'Key 9db5df9cf5a5434d9e50951d978c0314'}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response.status_code
    print(response.content)

    return render_template('home.html', results="response", data=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)
