from module.protocol.network.message import Message


class AllianceInvitationStateRecruterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4543
        self.recrutedName = {"type": "String", "value": ""}
