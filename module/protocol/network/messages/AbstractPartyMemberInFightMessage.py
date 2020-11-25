from module.protocol.network.message import Message


class AbstractPartyMemberInFightMessage(Message):
    def __init__(self):
        self.id = 3450
        self.memberName = {"type": "String", "value": ""}
