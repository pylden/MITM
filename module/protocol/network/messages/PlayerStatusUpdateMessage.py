from module.protocol.network.message import Message


class PlayerStatusUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2354
        self.accountId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.status = {"type": "PlayerStatus", "value": ""}
