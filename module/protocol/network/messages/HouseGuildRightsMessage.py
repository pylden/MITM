from module.protocol.network.message import Message


class HouseGuildRightsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8382
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.guildInfo = {"type": "GuildInformations", "value": ""}
        self.rights = {"type": "uint", "value": ""}
