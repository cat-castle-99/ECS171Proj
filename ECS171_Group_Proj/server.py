#server. py
#This is our controller file.
#It's responsibilities are:
    #Handling the relationship between the View files and the Model files
    #Passing input to the View to the Model
    #Passing output from the Model to the View
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


#Upper just capitalizes the message
def checkValid(sex, ch, restecg, exang, slope, ca ,thal):
    invalidAttributes = []
    if sex not in ['0','1']:
        invalidAttributes.append('sex')
    if ch not in ['0', '1', '2', '3']:
        invalidAttributes.append('chest pain')
    if restecg not in ['0', '1', '2']:
        invalidAttributes.append('resting electrocardiographic results')
    if exang not in ['y', 'n']:
        invalidAttributes.append('exercise induced angina')
    if slope not in ['0', '1', '2']:
        invalidAttributes.append('slope')
    if ca not in ['0', '1', '2', '3']:
        invalidAttributes.append('colored major vessels')
    if thal not in ['1', '2', '7']:
        invalidAttributes.append('thalium tracer')
    print(invalidAttributes)
    return invalidAttributes

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
    ch = request.form['ch']
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
    invalidFeat = checkValid(sex, ch, restecg, exang, slope, ca ,thal)
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
        print("All seems to be well")
        result = {
            "output": "All good"
        }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
