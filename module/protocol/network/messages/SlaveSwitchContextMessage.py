from module.protocol.network.message import Message


class SlaveSwitchContextMessage(Message):
    def __init__(self):
        self.id = 9736
