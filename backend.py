from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DEEPL_API_KEY = "YOUR_DEEPL_API_KEY"  # 여기에 DeepL API 키를 입력하세요.

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text")  # 사용자 입력 텍스트
    target_lang = data.get("target_lang")  # 번역 대상 언어

    # DeepL API 호출
    url = "https://api-free.deepl.com/v2/translate"
    payload = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "target_lang": target_lang
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
