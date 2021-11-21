"""
 * Project Name : sashArcade
 * Project repository link : https://github.com/sashwat-project-software/sash-arcade
 * File name : settings.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Created on : 20 November 2021
 * Last updated : 21 November 2021
 * Purpose : Defines the global settings for the game
"""

import os


class AppGlobals:
    """Defines all the global variables needed for the application"""

    def __init__(self):
        """ Defines global variables
        """
        self.__app_info()
        self.__app_settings()
        self.__operation_global_variables()

    def __app_info(self) -> None:
        """ Defines all the app information

        :return: None
        """
        self.__app_name__ = "sashArcade"
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
        self.app_title = "SashArcade :: Simple set of FOSS games"
        self.app_width_x = 500
        self.app_height_y = 300
        self.app_padding_x = 50
        self.app_padding_y = 50
        # About Window Settings
        self.app_about_title = f"{self.app_title} :: About Us"
        self.app_about_width_x = 0
        self.app_about_height_y = 0

    def __operation_global_variables(self) -> None:
        """ Definition to define app global variables

        :return: None
        """
        self.app_path = os.path.dirname(os.path.dirname(__file__))
        self.settings_path = os.path.join(self.app_path, "settings", "settings.json")
