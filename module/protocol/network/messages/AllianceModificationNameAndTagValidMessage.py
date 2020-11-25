from module.protocol.network.message import Message


class AllianceModificationNameAndTagVal8421(Message):
    def __init__(self):
        self.id = 8421
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
