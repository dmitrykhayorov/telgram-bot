import requests


def transale_cortex(input_str: str, source_lang: str, target_lang: str, token) -> str:

    url = "https://api.textcortex.com/v1/texts/translations"

    payload = {
        "source_lang": source_lang,
        "target_lang": target_lang,
        "text": input_str
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return (response.json()['data']['outputs'][0]['text'])
