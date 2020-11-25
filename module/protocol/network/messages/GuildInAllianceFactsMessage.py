from module.protocol.network.message import Message


class GuildInAllianceFactsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3384
        self.allianceInfos = {"type": "BasicNamedAllianceInformations", "value": ""}
