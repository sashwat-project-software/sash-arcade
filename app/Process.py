import os
import platform
import subprocess
import webbrowser

from settings import settings

settings = settings.AppGlobals()


class Process:
    def __init__(self):
        pass

    @staticmethod
    def open_json_file(filename) -> None:
        if platform.system() == "Darwin":
            subprocess.call(("open", filename))
        elif platform.system() == "Windows":
            os.startfile(filename)
        else:
            subprocess.call(('xdg-open', filename))

    @staticmethod
    def open_doc_link() -> None:
        webbrowser.open(settings.__project_wiki_link__, new=2)

    @staticmethod
    def open_project_link() -> None:
        webbrowser.open(settings.__project_link__, new=2)
