from module.protocol.network.message import Message


class GuildChangeMemberParametersMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2513
        self.memberId = {"type": "Number", "value": ""}
        self.rank = {"type": "uint", "value": ""}
        self.experienceGivenPercent = {"type": "uint", "value": ""}
        self.rights = {"type": "uint", "value": ""}
