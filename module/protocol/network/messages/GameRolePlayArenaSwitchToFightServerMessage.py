from module.protocol.network.message import Message


class GameRolePlayArenaSwitchToFightServerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9880
        self.address = {"type": "String", "value": ""}
        self.ports = {"type": "Vector.<uint>", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
