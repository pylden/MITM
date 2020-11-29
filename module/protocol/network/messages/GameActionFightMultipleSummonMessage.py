from module.protocol.network.messages.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightMultipleSummonMessage(AbstractGameActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractGameActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4979
        self.vars.append({"name": "summons", "type": "Vector.<GameContextSummonsInformation>", "value": ""})
