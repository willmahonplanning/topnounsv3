from flask import Flask, request, jsonify
from nltk import pos_tag, word_tokenize

app = Flask(__name__)

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.json['text']
    appended_text = append_top_to_nouns(text)
    return jsonify(appended_text=appended_text)

def append_top_to_nouns(text):
    appended_text = ""
    for word, pos in pos_tag(word_tokenize(text)):
        if pos[0] == 'N':
            appended_text += word + "top "
        else:
            appended_text += word + " "
    return appended_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
