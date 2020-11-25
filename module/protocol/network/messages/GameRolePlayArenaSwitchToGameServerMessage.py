from module.protocol.network.message import Message


class GameRolePlayArenaSwitchToGameServerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6269
        self.validToken = {"type": "Boolean", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
        self.homeServerId = {"type": "int", "value": ""}
