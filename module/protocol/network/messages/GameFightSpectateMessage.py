from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightSpectateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6511
        self.vars.append({"name": "effects", "type": "Vector.<FightDispellableEffectExtendedInformations>", "value": ""})
        self.vars.append({"name": "marks", "type": "Vector.<GameActionMark>", "value": ""})
        self.vars.append({"name": "gameTurn", "type": "uint", "value": ""})
        self.vars.append({"name": "fightStart", "type": "uint", "value": ""})
        self.vars.append({"name": "idols", "type": "Vector.<Idol>", "value": ""})
        self.vars.append({"name": "fxTriggerCounts", "type": "Vector.<GameFightEffectTriggerCount>", "value": ""})
