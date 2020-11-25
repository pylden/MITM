from module.protocol.network.message import Message


class AllianceModificationNameAndTagVal8421(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8421
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
