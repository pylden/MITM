from module.protocol.network.message import Message


class ZaapRespawnSaveRequestMessage(Message):
    def __init__(self):
        self.id = 4551
