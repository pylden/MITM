from module.protocol.network.message import Message


class PauseDialogMessage(Message):
    def __init__(self):
        self.id = 6004
