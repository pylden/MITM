from module.protocol.network.message import Message


class AllianceModificationVal8871(Message):
    def __init__(self):
        self.id = 8871
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
