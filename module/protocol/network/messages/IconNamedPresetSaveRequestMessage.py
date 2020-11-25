from module.protocol.network.message import Message


class IconNamedPresetSaveRequestMessage(Message):
    def __init__(self):
        self.id = 9336
        self.name = {"type": "String", "value": ""}
