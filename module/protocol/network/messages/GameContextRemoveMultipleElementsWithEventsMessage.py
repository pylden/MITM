from module.protocol.network.messages.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage


class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameContextRemoveMultipleElementsMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6586
        self.elementEventIds = {"type": "Vector.<uint>", "value": ""}
