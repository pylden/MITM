from module.injector.injector import Injector
from module.connexion.server_manager import ServerManager
from module.protocol.processor.d2_protocol import D2Protocol
from module.pluger.FrameClientPluger import FrameClientPluger
from module.ui.app import App
import queue
from module.protocol.network.messages.IdentificationMessage import IdentificationMessage
from module.io.bytes_reader import BytesReader

EXE_PATH = "C:/Users/Pierre/AppData/Local/Ankama/zaap/dofus/Dofus.exe"
EXE_NAME = "Dofus.exe"
LOCAL_SERVER_IP = "127.0.0.1"
LOCAL_SERVER_PORT = 5555
DISTANT_SERVER_IP = ["34.252.21.81", "52.17.231.202", "63.34.214.78"]
DISTANT_SERVER_PORT = 5555

# msg = IdentificationMessage(
#     BytesReader(bytes.fromhex("0102390a0000000f00000266728002702ef9aa7a8da08756c2a3cbb82495a4e87f2f5b5567ef55e1f07cba34e2185ef3d6aa0871c489ec973fe170a498df4c6e3151eeb871fc6f39065de15aa8248c53f3f750c0dec6bce6dc7441672f7d928fc6dbc281704999ed88b8168655c9eceae5c2cf69afc7edfb4ab81463d529e79e3430dbdfeacdc461b6d6a57ae649c40e64c0cc5af94c93dd7a68421dda3472998179ca39974bc72bf7cc7a1e53d15e9223bc64391ada92da30f47e976b3bf4d03186104dd212ccccea82793fb9b59e2ef81a6046905f5fc6a463a6ac4cf73264555e7625cd545cb12d78ec8b1fb18f0cab5f52bfb25efaae7a32a76d029a8daa9f78c4e3968adc3601f5d9ec0aadc90000000000")),
#     2,
#     276,
#     3
# )
#
# msg.deserialize()
# print(msg)

def main():
    # Inject DLL
    js_inject_connect_file = open("./ressources/frida_js/inject_connect.js", "r")
    js_inject_connect = js_inject_connect_file.read()
    js_inject_connect_file.close()
    injector = Injector(EXE_NAME, js_inject_connect, EXE_PATH)
    injector.start_and_inject()
    #injector.inject_all()

    # CREATE SERVER
    server_manager = ServerManager(LOCAL_SERVER_IP,
                                   LOCAL_SERVER_PORT,
                                   DISTANT_SERVER_IP[0],
                                   DISTANT_SERVER_PORT,
                                   D2Protocol)
    server_manager.start_server_in_thread()

    # CREATE PLUGER
    # q = queue.Queue()
    # FrameClientPluger(q).start()

    # START GUI
    # gui = App()
    # gui.mainloop()


if __name__ == "__main__":
    main()
