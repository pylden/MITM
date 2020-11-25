from module.protocol.network.message import Message


class GameRolePlayArenaSwitchToFightServerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9880
        self.address = {"type": "String", "value": ""}
        self.ports = {"type": "Vector.<uint>", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
