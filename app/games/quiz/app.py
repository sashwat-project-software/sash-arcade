"""
 * Project Name : sashArcade
 * Project repository link : https://github.com/sashwat-project-software/sash-arcade
 * File name : quiz.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Created on : 21 November 2021
 * Last updated : 21 November 2021
 * Purpose : Quiz game
"""

# Global Libraries
import tkinter
import html
# Local Libraries
from settings import settings

# Global variables
settings = settings.AppGlobals()


class QuizInterface:
    """"""
    def __init__(self):
        self.window = tkinter.Tk()
        # defines window specifications
        self.__define_window_settings()
        # Defines labels
        self.__define_labels()
        self.window.mainloop()

    def __define_window_settings(self) -> None:
        """ Defines window parameters

        :return: None
        """
        self.window.title(settings.app_title)
        self.window.config(padx=settings.app_padding_x, pady=settings.app_padding_y, bg=settings.window_bg_color)

    def __define_labels(self) -> None:
        """ Defines all the labels used

        :return:
        """
        self.header_label = tkinter.Label(
            text="Its Quiz time!!", fg=settings.window_fg_color, bg=settings.window_bg_color, font=settings.header)
        self.header_label.grid(row=0, column=0, columnspan=2)
        self.username = tkinter.Label(
            text="Sashwat K", fg=settings.window_fg_color, bg=settings.window_bg_color, font=settings.score_font)
        self.username.grid(row=1, column=0, pady=20)
        self.score_label = tkinter.Label(
            text="Score: 0", fg=settings.window_fg_color, bg=settings.window_bg_color, font=settings.score_font)
        self.score_label.grid(row=1, column=1, pady=20)
        self.canvas = tkinter.Canvas(width=300, height=250, bg=settings.canvas_bg_color)
        self.question_text = self.canvas.create_text(
            150, 125, text="Welcome to quiz game!!", fill=settings.canvas_fg_color, font=settings.question_font)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.true_image = tkinter.PhotoImage(file=settings.true_image_path)
        self.true_button = tkinter.Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(row=3, column=0)
        self.false_image = tkinter.PhotoImage(file=settings.false_image_path)
        self.false_button = tkinter.Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(row=3, column=1)


def main():
    QuizInterface()


if __name__ == '__main__':
    main()
