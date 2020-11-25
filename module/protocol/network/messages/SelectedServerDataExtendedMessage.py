from module.protocol.network.message import Message


class SelectedServerDataExtendedMessage(Message):
    def __init__(self):
        self.id = 8204
