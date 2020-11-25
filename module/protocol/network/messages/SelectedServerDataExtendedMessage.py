from module.protocol.network.message import Message


class SelectedServerDataExtendedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8204
        self.servers = {"type": "Vector.<GameServerInformations>", "value": ""}
