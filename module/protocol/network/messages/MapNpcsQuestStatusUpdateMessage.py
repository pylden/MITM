from module.protocol.network.message import Message


class MapNpcsQuestStatusUpdateMessage(Message):
    def __init__(self):
        self.id = 1168
