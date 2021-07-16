from flask import Flask, render_template, url_for, request
import pickle

# load the model from disk
clf = pickle.load(open('finalized_model.pkl', 'rb'))
cv = pickle.load(open('w2v_model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        # Word2Vec predict for each word we need to break the sentence
        sentence_split = message.split()
        data = []

        for i in sentence_split:
            if i in cv.wv:
                data.append(i)

        vect = cv.wv[data]
        my_prediction = clf.predict(vect)
        prediction = 0
        for i in my_prediction:
            if i == 1:
                prediction = 1

    return render_template('result.html', prediction=int(prediction))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
