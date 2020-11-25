from module.protocol.network.message import Message


class HouseGuildRightsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8382
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.guildInfo = {"type": "GuildInformations", "value": ""}
        self.rights = {"type": "uint", "value": ""}
