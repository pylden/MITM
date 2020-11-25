from module.protocol.network.message import Message


class AllianceCreationVal8739(Message):
    def __init__(self):
        self.id = 8739
        self.allianceName = {"type": "String", "value": ""}
        self.allianceTag = {"type": "String", "value": ""}
