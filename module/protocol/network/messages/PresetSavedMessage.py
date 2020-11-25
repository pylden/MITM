from module.protocol.network.message import Message


class PresetSavedMessage(Message):
    def __init__(self):
        self.id = 4545
