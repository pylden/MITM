from module.protocol.network.message import Message


class ObjectErrorMessage(Message):
    def __init__(self):
        self.id = 5736
