import numpy as np
import pickle
from flask import Flask , request , render_template

app = Flask(__name__ , template_folder= 'templates')

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def base():
    return render_template('form.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods = ['GET'])
def predict():
    
    age = request.args.get('age')

    gender = request.args.get('gender')

    stream = request.args.get('stream')

    internship = request.args.get('internship')

    cgpa = request.args.get('cgpa')

    hostel = request.args.get('hostel')

    backlogs = request.args.get('backlogs')

    arr = np.array([age,gender,stream,internship,cgpa,hostel,backlogs] , dtype = int)

    output = model.predict([arr])

    if(output==1):

        out = 'High'
        #out = f"Your Chances Of Getting Placed {model.predict_proba([arr])[0][1] * 100 :.2f} %"

    else:

        out = 'Low'
        #out =f"Your Chances Of Getting Placed {model.predict_proba([arr])[0][1] * 100 :.2f} %"
    
    return render_template('output.html', output=out)



if __name__ == '__main__':
    app.run(debug=True)

