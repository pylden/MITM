from module.protocol.network.message import Message


class AbstractPartyMemberInFightMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3450
        self.memberName = {"type": "String", "value": ""}
