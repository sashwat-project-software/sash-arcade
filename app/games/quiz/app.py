"""
 * Project Name : sashArcade
 * Project repository link : https://github.com/sashwat-project-software/sash-arcade
 * File name : quiz.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Created on : 21 November 2021
 * Last updated : 21 November 2021
 * Purpose : Quiz game
"""

import tkinter
# Global variables for App
settings = AppGlobals()


def quiz():
    window = tkinter.Tk()
    # Define tkinter settings
    window.title(settings.app_title)
    window.config(padx=settings.app_padding_x, pady=settings.app_padding_y)
    window.mainloop()