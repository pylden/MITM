from module.protocol.network.message import Message


class PresetDeleteResultMessage(Message):
    def __init__(self):
        self.id = 9792
