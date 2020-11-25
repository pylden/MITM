from module.protocol.network.message import Message


class SelectedServerDataMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6182
        self.serverId = {"type": "uint", "value": ""}
        self.address = {"type": "String", "value": ""}
        self.ports = {"type": "Vector.<uint>", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
