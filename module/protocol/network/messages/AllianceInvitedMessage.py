from module.protocol.network.message import Message


class AllianceInvitedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6002
        self.recruterId = {"type": "Number", "value": ""}
        self.recruterName = {"type": "String", "value": ""}
        self.allianceInfo = {"type": "BasicNamedAllianceInformations", "value": ""}
