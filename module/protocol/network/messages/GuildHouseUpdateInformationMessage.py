from module.protocol.network.message import Message


class GuildHouseUpdateInformationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6190
        self.housesInformations = {"type": "HouseInformationsForGuild", "value": ""}
