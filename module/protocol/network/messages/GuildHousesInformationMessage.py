from module.protocol.network.message import Message


class GuildHousesInformationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 872
        self.housesInformations = {"type": "Vector.<HouseInformationsForGuild>", "value": ""}
