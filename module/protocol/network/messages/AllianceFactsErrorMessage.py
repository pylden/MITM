from module.protocol.network.message import Message


class AllianceFactsErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2007
        self.allianceId = {"type": "uint", "value": ""}
