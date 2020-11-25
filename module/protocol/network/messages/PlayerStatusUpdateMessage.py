from module.protocol.network.message import Message


class PlayerStatusUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2354
        self.accountId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.status = {"type": "PlayerStatus", "value": ""}
