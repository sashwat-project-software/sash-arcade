import requests
from settings import settings
import html

# Global variables
settings = settings.AppGlobals()


class Process:
    def __init__(self) -> None:
        self.questions = self.__get_data_from_api()

    @staticmethod
    def __get_data_from_api() -> list:
        response = requests.get(settings.quiz_api_url, settings.api_parameters)
        data = response.json()
        ques_ans_list = []
        for i in data["results"]:
            temp = {
                "question": html.unescape(i["question"]),
                "answer": bool(i["correct_answer"])
            }
            ques_ans_list.append(temp)
        return ques_ans_list


Process()
