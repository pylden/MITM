from module.protocol.network.message import Message


class AllianceModificationVal8871(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8871
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
