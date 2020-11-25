from module.protocol.network.message import Message


class HaapiConfirmationRequestMessage(Message):
    def __init__(self):
        self.id = 3477
