"""
 * Project Name : sashArcade
 * Project repository link : https://github.com/sashwat-project-software/sash-arcade
 * File name : app.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Created on : 20 November 2021
 * Last updated : 21 November 2021
 * Purpose : Defines the global settings for the game
"""

# App Local Libraries
from settings.settings import AppGlobals
from AppUi import AppUi


# Global variables for App
settings = AppGlobals()
game_data = []


def main() -> None:
    """Main Definition"""
    ui = AppUi()


if __name__ == '__main__':
    main()
