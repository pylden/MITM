from module.protocol.network.message import Message


class PresetSaveErrorMessage(Message):
    def __init__(self):
        self.id = 8976
