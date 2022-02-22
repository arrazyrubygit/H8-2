import flask

import numpy as np
import pickle

model = pickle.load(open('C:/Users/rromy/Tutorial Python/Hacktiv8/FINAL PROJECT 1/model/model_linear.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    features = [x for x in flask.request.form.values()]
    new_features1 = [float(x) for x in features[0:2]]
    new_features2 = [int(i) if i.isdigit() else i for i in map(str, str(features[2]))]
    final_features = [np.append(new_features1, new_features2)]    
    prediction = model.predict(final_features)



    return flask.render_template('main.html', prediction_text='Harga taxi online adalah {}'.format(prediction[0]))