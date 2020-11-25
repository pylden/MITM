from module.protocol.network.message import Message


class MapRunningFightListRequestMessage(Message):
    def __init__(self):
        self.id = 7756
