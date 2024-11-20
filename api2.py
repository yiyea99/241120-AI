from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DEEPL_API_KEY = "YOUR_API_KEY"  # 발급받은 DeepL API 키

@app.route("/")
def home():
    return """
    <h1>DeepL 번역 챗봇</h1>
    <form action="/translate" method="post">
        <input type="text" name="text" placeholder="번역할 텍스트 입력">
        <select name="target_language">
            <option value="KO">한국어</option>
            <option value="EN">영어</option>
            <option value="JA">일본어</option>
        </select>
        <button type="submit">번역</button>
    </form>
    """

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text"]
    target_language = request.form["target_language"]
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
