from module.protocol.network.message import Message


class AllianceInvitationStateRecruterMessage(Message):
    def __init__(self):
        self.id = 4543
        self.recrutedName = {"type": "String", "value": ""}
