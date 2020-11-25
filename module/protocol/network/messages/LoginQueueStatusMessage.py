from module.protocol.network.message import Message


class LoginQueueStatusMessage(Message):
    def __init__(self):
        self.id = 7010
