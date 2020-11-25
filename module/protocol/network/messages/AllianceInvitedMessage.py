from module.protocol.network.message import Message


class AllianceInvitedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6002
        self.recruterId = {"type": "Number", "value": ""}
        self.recruterName = {"type": "String", "value": ""}
        self.allianceInfo = {"type": "BasicNamedAllianceInformations", "value": ""}
