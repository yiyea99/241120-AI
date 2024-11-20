import requests

def deepl_translate(text, target_language="KO", source_language=None):
    api_key = "YOUR_API_KEY"  # DeepL에서 발급받은 API 키
    url = "https://api-free.deepl.com/v2/translate"

    # 요청 데이터 구성
    data = {
        "auth_key": api_key,
        "text": text,
        "target_lang": target_language
    }
    if source_language:
        data["source_lang"] = source_language

    # API 호출
    response = requests.post(url, data=data)

    if response.status_code == 200:
        result = response.json()
        return result["translations"][0]["text"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# 예제 사용법
text_to_translate = "Hello, how are you?"
translated_text = deepl_translate(text_to_translate, target_language="KO")
print(f"번역 결과: {translated_text}")
