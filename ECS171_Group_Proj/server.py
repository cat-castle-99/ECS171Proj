#server. py
#This is our controller file.
#It's responsibilities are:
    #Handling the relationship between the View files and the Model files
    #Passing input to the View to the Model
    #Passing output from the Model to the View
from flask import Flask, request, render_template, jsonify
import os
from Runtime import logModel, userinput, myModel

app = Flask(__name__)


#Upper just capitalizes the message
def checkValid(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    invalidAttributes = []
    try:
        int(round(float(age)))
    except:
        invalidAttributes.append('age')
    if sex not in ['0','1']:
        invalidAttributes.append('sex')
    if cp not in ['0', '1', '2', '3']:
        invalidAttributes.append('chest pain')
    try:
        int(round(float(trestbps)))
    except:
        invalidAttributes.append('resting blood pressure')
    try:
        int(round(float(chol)))
    except:
        invalidAttributes.append('serum cholesterol')
    try:
        int(round(float(fbs)))
    except:
        invalidAttributes.append('fasting blood sugar')
    if restecg not in ['0', '1', '2']:
        invalidAttributes.append('resting electrocardiographic results')
    try:
        int(round(float(thalach)))
    except:
        invalidAttributes.append('maximum heart rate achieved')
    if exang not in ['y', 'n']:
        invalidAttributes.append('exercise induced angina')
    try:
        float(oldpeak)
    except:
        invalidAttributes.append('ST depression induced by exercise relative to rest')
    if slope not in ['0', '1', '2']:
        invalidAttributes.append('slope')
    if ca not in ['0', '1', '2', '3']:
        invalidAttributes.append('colored major vessels')
    if thal not in ['1', '2', '3']:
        invalidAttributes.append('thalium tracer')
    print(invalidAttributes)
    return invalidAttributes

def convertInput(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # TODO not sure if should be dictionary format tbh, but using dictionary for now
    # rounding numberical input as well for age, trestbps, chol, fbs, and thalach
    data = {}
    data['age'] = int(round(float(age)))
    data['sex'] = int(sex)
    data['cp'] = int(cp)
    data['trestbps'] = int(round(float(trestbps)))
    data['chol'] = int(round(float(chol)))
    data['fbs'] = int(round(float(fbs)))
    data['restecg'] = int(restecg)
    data['thalach'] = int(round(float(thalach)))
    data['exang'] = 1
    if exang == 'y':
        data['exang'] = 1
    else:
        data['exang'] = 0
    data['oldpeak'] = float(oldpeak)
    data['slope'] = int(slope)
    data['ca'] = int(ca)
    data['thal'] = int(thal)
    return data

#The app.route references the url referenced, yes AJAX requests are using the url to make the HTTP request
#this means that everytime you type a url you're also making an HTTP request
#idk if this is too much detail

@app.route('/')
def home():
    print(userinput)
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

    #need to check validity of sex, ch, restecg, exang, slope, ca, thal
    #FIXME: need to also check that oldpeak is a proper decimal
    invalidFeat = checkValid(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    #Data is sent to and from the sides as a JSON. In this example, it's just sending the combined form of our input back to the client side
    #In the future, we'll replace that do_someething() function with a function that parses the JSON for the model
    #Then, after running the model, we'll put the output from the model into a new JSON that we'll send back to the client-side
    if invalidFeat:
        #some value is incorrect
        print("Something was found to be incorrect")
        tempString = ''
        for i in invalidFeat:
            tempString += i
            tempString += ', '
        tempString = tempString[:-2]
        result = {
            "output1": "There are some problems with inputs for ",
            "output2": tempString
        }
    #FIXME: change this to the part where we input the data into the model, and put result of model in output
    #o yea also? need to change exang to something numerical maybes
    else:
        # TODO - right now this returns a dictionary, also unsure if it is being normalized in backend somehow?
        data_input = convertInput(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        print("All seems to be well")
        print(data_input)
        result = {
            "data": data_input

        }
    result = {str(key): value for key, value in result.items()}
    print("The result is...")
    print(result["data"])
    prediction = myModel.makePrediction(result["data"])
    result["data"]["prediction"] = int(prediction)
    print(result)
    myModel.generateGraph(result["data"])
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=False)
