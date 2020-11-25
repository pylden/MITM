from module.protocol.network.message import Message


class GameFightSpectateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6511
        self.effects = {"type": "Vector.<FightDispellableEffectExtendedInformations>", "value": ""}
        self.marks = {"type": "Vector.<GameActionMark>", "value": ""}
        self.gameTurn = {"type": "uint", "value": ""}
        self.fightStart = {"type": "uint", "value": ""}
        self.idols = {"type": "Vector.<Idol>", "value": ""}
        self.fxTriggerCounts = {"type": "Vector.<GameFightEffectTriggerCount>", "value": ""}
