from flask import Flask, render_template
from Model import analyze_text_with_emoji
from flask import request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    emoji_result = None
    if request.method == 'POST':
        user_text = request.form.get('text')
        emoji_result = analyze_text_with_emoji(user_text)
    return render_template('Main.html', emoji_result=emoji_result)

if __name__ == '__main__':
    app.run(debug=True)