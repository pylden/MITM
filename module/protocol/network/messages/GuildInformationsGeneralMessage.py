from module.protocol.network.message import Message


class GuildInformationsGeneralMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5234
        self.abandonnedPaddock = {"type": "Boolean", "value": ""}
        self.level = {"type": "uint", "value": ""}
        self.expLevelFloor = {"type": "Number", "value": ""}
        self.experience = {"type": "Number", "value": ""}
        self.expNextLevelFloor = {"type": "Number", "value": ""}
        self.creationDate = {"type": "uint", "value": ""}
        self.nbTotalMembers = {"type": "uint", "value": ""}
        self.nbConnectedMembers = {"type": "uint", "value": ""}
