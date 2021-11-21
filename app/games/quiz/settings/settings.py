"""
 * Project Name : sashArcade
 * Project repository link : https://github.com/sashwat-project-software/sash-arcade
 * File name : settings.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Created on : 20 November 2021
 * Last updated : 21 November 2021
 * Purpose : Quiz game
"""

import os


class AppGlobals:
    """Defines all the global variables needed for the application"""

    def __init__(self):
        """Defines all the global variables needed for the application"""
        self.__app_info()
        self.__app_settings()
        self.__get_quiz_data()
        self.__operation_global_variables()

    def __app_info(self):
        """

        :return:
        """
        self.__app_name__ = "sashArcade :: Quiz"
        self.__author__ = "Sashwat K"
        self.__license__ = "GPL"
        self.__version__ = "0.0.1"
        self.__maintainer__ = "Sashwat K"
        self.__email__ = "sashwat0001@gmail.com"
        self.__project_link__ = "https://github.com/sashwat-project-software/sash-arcade"
        self.__project_wiki_link__ = "https://github.com/sashwat-project-software/sash-arcade/wiki"

    def __app_settings(self) -> None:
        """ Defines global UI settings for the application

        :return: None
        """
        # Main Windows Settings
        self.app_title = "SashArcade :: Quiz"
        self.app_width_x = 500
        self.app_height_y = 300
        self.app_padding_x = 50
        self.app_padding_y = 50
        self.window_bg_color = "#483434"
        self.window_fg_color = "#EED6C4"
        self.canvas_bg_color = "#6B4F4F"
        self.canvas_fg_color = "#FFF3E4"
        self.header = ("Arial", 22, "bold")
        self.score_font = ("Arial", 14, "bold")
        self.question_font = ("Arial", 20, "italic")
        self.window_title = "Its Quiz time!!"

    def __get_quiz_data(self) -> None:
        """ """
        self.available_quiz_categories = {
            "General Knowledge": 9,
            "Entertainment: Film": 11,
            "Entertainment: Video Games": 15,
            "Science and Nature": 17,
            "Science: Computers": 18,
            "Sports": 21,
            "Animals": 27,
            "vehicles": 28
        }
        self.quiz_difficulty = ["easy", "medium", "hard"]
        self.max_question_count = 50

    def __operation_global_variables(self) -> None:
        """ Definition to define app global variables

        :return: None
        """
        self.app_path = os.path.dirname(os.path.dirname(__file__))
        self.true_image_path = os.path.join(self.app_path, "assets", "true.png")
        self.false_image_path = os.path.join(self.app_path, "assets", "false.png")
        self.settings_path = os.path.join(self.app_path, "settings", "settings.json")
        self.quiz_api_url = "https://opentdb.com/api.php"
        self.selected_quiz_category = self.available_quiz_categories["Science: Computers"]
        self.selected_quiz_difficulty = self.quiz_difficulty[0]
        self.quiz_number_of_questions = 10
        self.api_parameters = {
            "amount": self.quiz_number_of_questions,
            "type": "boolean",
            "category": self.selected_quiz_category,
            "difficulty": self.selected_quiz_difficulty
        }
        self.user_name = ""
        self.final_score = 0
        self.no_of_correct_ans = 0
        self.no_of_wrong_ans = 0
