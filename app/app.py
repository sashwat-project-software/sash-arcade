"""
 * Project Name : sashArcade
 * Project repository link : https://github.com/sashwat-project-software/sash-arcade
 * File name : app.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Created on : 20 November 2021
 * Last updated : 21 November 2021
 * Purpose : Defines the global settings for the game
"""

# Global Libraries
import tkinter
import os
import webbrowser
# App Local Libraries
from settings import AppGlobals

# Global Variables for UI
title_label_main_name = "Welcome to SashArcade"
title_label_sub_name = "A collection for small games!"
title_main_font = ("Arial", 24, "bold")
title_sub_font = ("Arial", 18, "italic")
table_header_font = ("Arial", 14, "bold")
table_row_font = ("Arial", 14)
# Global variables for App
settings = AppGlobals()
game_data = []


def main() -> None:
    """Main Definition"""
    global settings
    window = tkinter.Tk()
    # Define tkinter settings
    window.title(settings.app_title)
    window.config(padx=settings.app_padding_x, pady=settings.app_padding_y)
    # Menubar
    menubar = tkinter.Menu(window)
    app_help = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=app_help)
    app_help.add_command(label=f"About {settings.__app_name__}", command=None)
    app_help.add_command(label="View Documentation", command=open_doc_link)
    app_help.add_command(label="View Project in GitHub", command=open_project_link)
    window.config(menu=menubar)
    # Defines labels
    window_labels()
    # Defines tkinter window loop
    window.mainloop()


def open_doc_link() -> None: webbrowser.open(settings.__project_wiki_link__, new=2)


def open_project_link() -> None: webbrowser.open(settings.__project_link__, new=2)


def window_labels() -> None:
    """Definition to define main windows's labels

    :return: None
    """
    global game_data
    title_label = tkinter.Label(text=title_label_main_name, font=title_main_font)
    title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    title_sub_label = tkinter.Label(text=title_label_sub_name, font=title_sub_font)
    title_sub_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
    generate_table()


def generate_table() -> None:
    """ tkinter options to generate game table

    :return: None
    """
    global game_data
    table_header_sl = tkinter.Label(text="Sl No", font=table_header_font)
    table_header_sl.grid(row=2, column=0, padx=10, pady=10)
    table_header_logo = tkinter.Label(text="Game Logo", font=table_header_font)
    table_header_logo.grid(row=2, column=1, padx=10, pady=10)
    table_header_name = tkinter.Label(text="Game Name", font=table_header_font)
    table_header_name.grid(row=2, column=2, padx=10, pady=10)
    table_header_name = tkinter.Label(text="Option", font=table_header_font)
    table_header_name.grid(row=2, column=3, padx=10, pady=10)
    game_data = get_game_list()
    game_ui_dict = {}
    for index, data in enumerate(game_data):
        def action(x=data): open_game(x)
        row_dict = {
            "sl_no": tkinter.Label(text=index + 1, font=table_row_font),
            "logo": tkinter.Label(text="-", font=table_row_font),
            "game_name": tkinter.Label(text=data["game_name"], font=table_row_font),
            "play_button": tkinter.Button(text="Play!", command=action)
        }
        row_dict["sl_no"].grid(row=index + 3, column=0)
        row_dict["logo"].grid(row=index + 3, column=1)
        row_dict["game_name"].grid(row=index + 3, column=2)
        row_dict["play_button"].grid(row=index + 3, column=3)
        game_ui_dict[data["game_name"]] = row_dict


def open_game(game_name) -> None:
    """ Definition to open game

    :param game_name: dict of game to execute
    :return: None
    """
    print(f"{game_name}")


def get_game_list() -> list:
    """Returns the dict of available games

    :return: list of dict
    """
    global settings
    game_info = []
    game_path = os.path.join(settings.app_path, "games")
    for i in os.listdir(game_path):
        if os.path.isdir(os.path.join(game_path, i)):
            logo_path = os.path.join(game_path, i, "logo.png")
            game_py_path = os.path.join(game_path, i, "app.py")
            game_dict = {
                "game_name": i,
                "logo_path": logo_path if os.path.exists(logo_path) else None,
                "game_path": game_py_path if os.path.exists(game_py_path) else None
            }
            game_info.append(game_dict)
    return game_info


if __name__ == '__main__':
    main()
