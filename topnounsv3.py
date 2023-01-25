import nltk
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def topnounsv3():
    if request.method == 'POST':
        text = request.form['text']
        words = nltk.word_tokenize(text)
        tagged_words = nltk.pos_tag(words)
        topified_text = ""
        for word in tagged_words:
            if word[1] == 'NN':
                topified_text += "top" + word[0] + " "
            else:
                topified_text += word[0] + " "
        return render_template('index.html', topified_text=topified_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
