from module.protocol.network.message import Message


class IconPresetSaveRequestMessage(Message):
    def __init__(self):
        self.id = 6308
