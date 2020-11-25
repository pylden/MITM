from module.protocol.network.message import Message


class SelectedServerDataMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6182
        self.serverId = {"type": "uint", "value": ""}
        self.address = {"type": "String", "value": ""}
        self.ports = {"type": "Vector.<uint>", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
