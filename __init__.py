# from module.injector.injector import Injector
from module.connexion.server_manager import ServerManager
from module.protocol.processor.d2_protocol import D2Protocol
from module.pluger.FrameClientPluger import FrameClientPluger
from module.ui.app import App
import queue
import os
import re

EXE_PATH = "C:/Users/Pierre/AppData/Local/Ankama/zaap/dofus/Dofus.exe"
EXE_NAME = "Dofus.exe"
LOCAL_SERVER_IP = "127.0.0.1"
LOCAL_SERVER_PORT = 5555
DISTANT_SERVER_IP = ["34.252.21.81", "52.17.231.202", "63.34.214.78"]
DISTANT_SERVER_PORT = 5555


def main():
    pass

    # Inject DLL
    # js_inject_connect_file = open("./ressources/frida_js/inject_connect.js", "r")
    # js_inject_connect = js_inject_connect_file.read()
    # js_inject_connect_file.close()
    # injector = Injector(EXE_NAME, js_inject_connect, EXE_PATH)
    # injector.inject_all()

    # CREATE SERVER
    # server_manager = ServerManager(LOCAL_SERVER_IP,
    #                                LOCAL_SERVER_PORT,
    #                                DISTANT_SERVER_IP[0],
    #                                DISTANT_SERVER_PORT,
    #                                D2Protocol)
    # server_manager.start_server_in_thread()

    # CREATE PLUGER
    # q = queue.Queue()
    # FrameClientPluger(q).start()

    # START GUI
    # gui = App()
    # gui.mainloop()


if __name__ == "__main__":
    main()
