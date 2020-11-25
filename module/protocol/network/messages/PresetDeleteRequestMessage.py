from module.protocol.network.message import Message


class PresetDeleteRequestMessage(Message):
    def __init__(self):
        self.id = 7425
