from module.protocol.network.message import Message


class InteractiveUseErrorMessage(Message):
    def __init__(self):
        self.id = 9202
