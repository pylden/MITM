from module.protocol.network.message import Message


class AllianceKickRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9735
        self.kickedId = {"type": "uint", "value": ""}
