import time
from threading import Thread
from module.connexion.server_manager import Server


class FrameClientPluger(Thread):
    def __init__(self, q):
        Thread.__init__(self)
        self._q = q

    def run(self):
        while True:
            print("Waiting to plug...")
            frame = self._q.get()
            for r in range(5):
                print(len(Server.clients))
                for client in Server.clients:
                    if client['id'] is None:
                        client.protocol_processor.view = frame
                        frame.client_socket = client.protocol_processor
                        self._q.task_done()
                        break
                print("No dofus found")
                time.sleep(2)
