"""
 * Project Name : sashArcade
 * Project repository link : https://github.com/sashwat-project-software/sash-arcade
 * File name : app.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Created on : 20 November 2021
 * Last updated : 20 November 2021
 * Purpose : Defines the global settings for the game
"""

import tkinter
import os
from settings import AppGlobals

# Global Variables
title_label_main_name = "Welcome to SashArcade"
title_label_sub_name = "A collection for small games!"
title_main_font = ("Arial", 24, "bold")
title_sub_font = ("Arial", 18, "italic")
table_header_font = ("Arial", 14)


def main() -> None:
    """Main Definition"""
    window = tkinter.Tk()
    settings = AppGlobals()
    # Define tkinter settings
    window.title(settings.app_title)
    window.minsize(width=settings.app_width_x, height=settings.app_height_y)
    window.config(padx=settings.app_padding_x, pady=settings.app_padding_y)
    # Defines labels
    window_labels()
    # Defines tkinter window loop
    window.mainloop()


def window_labels() -> None:
    """
    Definition to define main windows's labels
    :return: None
    """
    title_label = tkinter.Label(text=title_label_main_name, font=title_main_font)
    title_label.grid(row=0, column=1, padx=20, pady=10)
    title_sub_label = tkinter.Label(text=title_label_sub_name, font=title_sub_font)
    title_sub_label.grid(row=1, column=1, padx=10, pady=5)
    table_header_sl = tkinter.Label(text="Sl No", font=table_header_font)
    table_header_sl.grid(row=2, column=0)
    table_header_logo = tkinter.Label(text="Game Logo", font=table_header_font)
    table_header_logo.grid(row=2, column=1)
    table_header_name = tkinter.Label(text="Game Name", font=table_header_font)
    table_header_name.grid(row=2, column=2)
    game_data = __get_game_list()


def __get_game_list() -> dict:
    game_info = {"game_name": "", "logo_path": ""}

    for i in os.listdir(os.path.join(os.path.dirname(__file__), "games")):
        print(i)
    return game_info


if __name__ == '__main__':
    main()
