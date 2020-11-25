from module.protocol.network.message import Message


class SelectedServerDataExtendedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8204
        self.servers = {"type": "Vector.<GameServerInformations>", "value": ""}
