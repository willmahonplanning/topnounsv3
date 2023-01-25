import nltk
nltk.download('averaged_perceptron_tagger')
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def topnounsv3():
    if request.method == 'POST':
        text = request.form['text']
        tokenized_text = nltk.word_tokenize(text)
        tagged_text = nltk.pos_tag(tokenized_text)
        modified_text = ""
        for word in tagged_text:
            if word[1] == "NN":
                modified_text += "top" + word[0] + " "
            else:
                modified_text += word[0] + " "
        return render_template('index.html', modified_text=modified_text)
    return render_template('index.html')

if __name__ == '__main__':
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    app.run()
