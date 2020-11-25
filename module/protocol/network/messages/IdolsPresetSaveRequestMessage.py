from module.protocol.network.message import Message


class IdolsPresetSaveRequestMessage(Message):
    def __init__(self):
        self.id = 1043
