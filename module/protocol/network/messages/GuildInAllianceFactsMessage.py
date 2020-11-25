from module.protocol.network.message import Message


class GuildInAllianceFactsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3384
        self.allianceInfos = {"type": "BasicNamedAllianceInformations", "value": ""}
