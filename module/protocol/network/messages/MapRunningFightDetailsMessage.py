from module.protocol.network.message import Message


class MapRunningFightDetailsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2688
        self.fightId = {"type": "uint", "value": ""}
        self.attackers = {"type": "Vector.<GameFightFighterLightInformations>", "value": ""}
        self.defenders = {"type": "Vector.<GameFightFighterLightInformations>", "value": ""}
