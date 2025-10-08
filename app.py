from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load summarizer model (you can change model here)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    if not text.strip():
        return render_template('index.html', summary="Please enter some text!")

    summary = summarizer(text, max_length=120, min_length=40, do_sample=False)
    return render_template('index.html', summary=summary[0]['summary_text'])

if __name__ == '__main__':
    app.run(debug=True)
