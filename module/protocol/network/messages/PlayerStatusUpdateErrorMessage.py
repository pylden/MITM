from module.protocol.network.message import Message


class PlayerStatusUpdateErrorMessage(Message):
    def __init__(self):
        self.id = 9102
