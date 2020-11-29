from module.protocol.network.messages.TreasureHuntDigRequestAnswerMessage import TreasureHuntDigRequestAnswerMessage


class TreasureHuntDigRequestAnswerFailedMessage(TreasureHuntDigRequestAnswerMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        TreasureHuntDigRequestAnswerMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5389
        self.vars.append({"name": "wrongFlagCount", "type": "uint", "value": ""})
