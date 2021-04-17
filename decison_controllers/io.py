from decison_controllers.speaker import speak, take_speech, speech_control, wish_me
import requests
from tabulate import tabulate


def decision_divider(query: str, reply: str):
    if '_' in reply:
        url = f"http://localhost:5001/api/v1/{reply}"
        data_obj = {"query": f"{query}"}
        result = requests.post(url, data=data_obj)
        result = result.json()

        if result["tune"] is True:
            print(result["data"])
            speak(result["data"])
        else:
            # data_type = type(result["data"])
            rd = result["data"]

            final_list = []
            if isinstance(rd, list):
                headers = list(rd[0].keys())
                for values in rd:
                    temp_tuple = ()
                    temp_lst = []
                    for head in headers:
                        temp_lst.append(values[f"{head}"])
                    temp_tuple = tuple(temp_lst)
                    final_list.append(temp_tuple)
                tabulate_result = tabulate(final_list, headers=headers)
                print(tabulate_result)
                speak("Sir here is your result")
            else:
                headers = list(rd.keys())
                pass
    else:
        speak(reply)
