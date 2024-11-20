from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

DEEPL_API_KEY = " "  # DeepL API 키

@app.route("/")
def home():
    return render_template("dic.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text")
    target_language = "EN" 

    url = "https://api-free.deepl.com/v2/translate"
    payload = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "target_lang": target_language
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        result = response.json()
        translated_text = result["translations"][0]["text"]
        return jsonify({"translatedText": translated_text})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
