#server. py
#This is our controller file.
#It's responsibilities are:
    #Handling the relationship between the View files and the Model files
    #Passing input to the View to the Model
    #Passing output from the Model to the View
from flask import Flask, request, render_template, jsonify
import sys
app = Flask(__name__)


#Upper just capitalizes the message
def do_something(text1,text2):
   text1 = text1.upper()
   combine = text1 + text2
   return combine

#The app.route references the url referenced, yes AJAX requests are using the url to make the HTTP request
#this means that everytime you type a url you're also making an HTTP request
#idk if this is too much detail

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getModelOutput', methods=['GET','POST'])
#any reference to "form" is referencing the JSON we passed in the post request
#on that note, the request referenced here is a data structure that contains relevant information sent with the HTTP request, including our JSON
#therefore: request.form = the JSON we sent
def my_form_post():
    age = request.form['age']
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']
    # below is original function with categ1 and numer1
    text1 = request.form['categ1']
    text2 = request.form['numer1']
    combine = do_something(text1,text2)
    #print("past combine", file=sys.stderr)
    #Data is sent to and from the sides as a JSON. In this example, it's just sending the combined form of our input back to the client side
    #In the future, we'll replace that do_someething() function with a function that parses the JSON for the model
    #Then, after running the model, we'll put the output from the model into a new JSON that we'll send back to the client-side
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
