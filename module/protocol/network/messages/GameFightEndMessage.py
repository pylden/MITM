from module.protocol.network.message import Message


class GameFightEndMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1090
        self.duration = {"type": "uint", "value": ""}
        self.rewardRate = {"type": "int", "value": ""}
        self.lootShareLimitMalus = {"type": "int", "value": ""}
        self.results = {"type": "Vector.<FightResultListEntry>", "value": ""}
        self.namedPartyTeamsOutcomes = {"type": "Vector.<NamedPartyTeamWithOutcome>", "value": ""}
