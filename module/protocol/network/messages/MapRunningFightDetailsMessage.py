from module.protocol.network.message import Message


class MapRunningFightDetailsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2688
        self.fightId = {"type": "uint", "value": ""}
        self.attackers = {"type": "Vector.<GameFightFighterLightInformations>", "value": ""}
        self.defenders = {"type": "Vector.<GameFightFighterLightInformations>", "value": ""}
