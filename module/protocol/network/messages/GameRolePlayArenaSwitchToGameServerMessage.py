from module.protocol.network.message import Message


class GameRolePlayArenaSwitchToGameServerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6269
        self.validToken = {"type": "Boolean", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
        self.homeServerId = {"type": "int", "value": ""}
