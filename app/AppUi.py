import tkinter
import tkinter.messagebox
import os
import subprocess

from settings.settings import AppGlobals
from Process import Process

# Global variables
settings = AppGlobals()
process_runner = Process()


class AppUi:
    def __init__(self) -> None:
        """"""
        self.window = tkinter.Tk()
        self.__define_window_settings()
        self.__define_menubar_settings()
        self.__window_labels()
        self.window.mainloop()

    def __define_window_settings(self) -> None:
        self.window.title(settings.app_title)
        self.window.config(padx=settings.app_padding_x, pady=settings.app_padding_y, bg=settings.window_bg_color)

    def __define_menubar_settings(self) -> None:
        def open_editor(x=settings.settings_path): process_runner.open_json_file(x)
        self.menubar = tkinter.Menu(self.window)
        self.app_file = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.app_file)
        self.app_file.add_command(label="Settings", command=open_editor)
        self.app_help = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.app_help)
        self.app_help.add_command(label=f"About {settings.__app_name__}", command=None)
        self.app_help.add_command(label="View Documentation", command=process_runner.open_doc_link)
        self.app_help.add_command(label="View Project in GitHub", command=process_runner.open_project_link)
        self.window.config(menu=self.menubar)

    def __window_labels(self) -> None:
        self.title_label = tkinter.Label(text=settings.title_label_main_name, font=settings.title_main_font,
                                         fg=settings.window_fg_color, bg=settings.window_bg_color)
        self.title_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.title_sub_label = tkinter.Label(text=settings.title_label_sub_name, font=settings.title_sub_font,
                                             fg=settings.window_fg_color, bg=settings.window_bg_color)
        self.title_sub_label.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        self.__generate_label_table()

    def __generate_label_table(self) -> None:
        self.table_header_sl = tkinter.Label(text="Sl No", font=settings.table_header_font,
                                             fg=settings.window_fg_color, bg=settings.window_bg_color)
        self.table_header_sl.grid(row=2, column=0, padx=10, pady=10)
        self.table_header_logo = tkinter.Label(text="Game Logo", font=settings.table_header_font,
                                               fg=settings.window_fg_color, bg=settings.window_bg_color)
        self.table_header_logo.grid(row=2, column=1, padx=10, pady=10)
        self.table_header_name = tkinter.Label(text="Game Name", font=settings.table_header_font,
                                               fg=settings.window_fg_color, bg=settings.window_bg_color)
        self.table_header_name.grid(row=2, column=2, padx=10, pady=10)
        self.table_header_name = tkinter.Label(text="Option", font=settings.table_header_font,
                                               fg=settings.window_fg_color, bg=settings.window_bg_color)
        self.table_header_name.grid(row=2, column=3, padx=10, pady=10, columnspan=2)
        self.game_data = self.__get_game_list()
        self.game_ui_dict = {}
        self.images = []
        for index, data in enumerate(self.game_data):
            def action_play(x=data): self.__open_game(x)
            def action_settings(x=data): self.__open_game_settings(x)
            image = tkinter.PhotoImage(file=data["logo_path"])
            image = image.subsample(4, 4)
            row_dict = {
                "sl_no": tkinter.Label(text=index + 1, font=settings.table_row_font, fg=settings.window_fg_color,
                                       bg=settings.window_bg_color),
                "logo": tkinter.Label(image=image, fg=settings.window_fg_color, bg=settings.window_bg_color),
                "game_name": tkinter.Label(text=data["game_name"], font=settings.table_row_font,
                                           fg=settings.window_fg_color, bg=settings.window_bg_color),
                "play_button": tkinter.Button(text="Play!", command=action_play, fg=settings.window_fg_color,
                                              bg=settings.window_bg_color, highlightthickness=0),
                "settings_button": tkinter.Button(text="settings", command=action_settings, fg=settings.window_fg_color,
                                                  bg=settings.window_bg_color, highlightthickness=0)
            }
            self.images.append(image)
            row_dict["sl_no"].grid(row=index + 3, column=0)
            row_dict["logo"].grid(row=index + 3, column=1)
            row_dict["game_name"].grid(row=index + 3, column=2)
            row_dict["play_button"].grid(row=index + 3, column=3)
            row_dict["settings_button"].grid(row=index + 3, column=4)
            self.game_ui_dict[data["game_name"]] = row_dict

    @staticmethod
    def __get_game_list() -> list:
        """ Returns the dict of available games

        :return: list of dict
        """
        game_info = []
        game_path = os.path.join(settings.app_path, "games")
        for i in os.listdir(game_path):
            if os.path.isdir(os.path.join(game_path, i)):
                logo_path = os.path.join(game_path, i, "logo.png")
                game_py_path = os.path.join(game_path, i, "app.py")
                game_setting_path = os.path.join(os.path.dirname(game_py_path), "settings", "settings.json")
                game_dict = {
                    "game_name": i,
                    "logo_path": logo_path if os.path.exists(logo_path) else None,
                    "game_path": game_py_path if os.path.exists(game_py_path) else None,
                    "game_settings": game_setting_path if os.path.exists(game_setting_path) else None
                }
                game_info.append(game_dict)
        return game_info

    @staticmethod
    def __open_game(game_dict_data) -> None:
        """ Definition to open game

        :param game_dict_data: dict of game to execute
        :return: None
        """
        process = subprocess.Popen(f"python3 {game_dict_data['game_path']}", shell=True)
        output, error = process.communicate()

    @staticmethod
    def __open_game_settings(game_name) -> None:
        """ Definition to open game's settings.json file in text editor

        :param game_name: dict of game to execute
        :return: None
        """
        tkinter.messagebox.showinfo(
            f"Opening {game_name['game_name']}",
            f"Opening game {game_name['game_name']} settings!!")
        process_runner.open_json_file(game_name["game_settings"])
