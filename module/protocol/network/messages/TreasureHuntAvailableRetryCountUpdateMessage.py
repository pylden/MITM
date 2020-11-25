from module.protocol.network.message import Message


class TreasureHuntAvailableRetryCountUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4986
        self.questType = {"type": "uint", "value": ""}
        self.availableRetryCount = {"type": "int", "value": ""}
