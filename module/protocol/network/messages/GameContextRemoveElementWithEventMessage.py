from module.protocol.network.messages.GameContextRemoveElementMessage import GameContextRemoveElementMessage


class GameContextRemoveElementWithEventMessage(GameContextRemoveElementMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameContextRemoveElementMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3832
        self.vars.append({"name": "elementEventId", "type": "uint", "value": ""})
