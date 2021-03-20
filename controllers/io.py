from controllers.speaker import speak, take_speech, speech_control, wish_me
import requests


def decision_divider(query: str, reply: str):
    if '_' in reply:
        url = f"http://localhost:5001/api/v1/{reply}"
        data_obj = {"query": f"{query}"}
        result = requests.post(url, data=data_obj)
        result = result.json()
        speak(result["data"])
    else:
        speak(reply)
