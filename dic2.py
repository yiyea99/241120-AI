from flask import Flask, request, render_template
import requests

app = Flask(__name__)

DEEPL_API_KEY = "YOUR_API_KEY"  # 발급받은 DeepL API 키

@app.route("/")
def home():
    return render_template("dic.html")

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text"]
    target_language = "EN"  # 항상 영어로 번역

    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "target_lang": target_language
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        result = response.json()
        translated_text = result["translations"][0]["text"]
        return f"<h1>번역 결과</h1><p>{translated_text}</p>"
    else:
        return f"<h1>Error</h1><p>{response.text}</p>"

if __name__ == "__main__":
    app.run(debug=True)
