from module.protocol.network.messages.GameFightEndMessage import GameFightEndMessage


class BreachGameFightEndMessage(GameFightEndMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameFightEndMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4165
        self.budget = {"type": "int", "value": ""}
