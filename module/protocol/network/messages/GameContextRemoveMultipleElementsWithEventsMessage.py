from module.protocol.network.message import Message


class GameContextRemoveMultipleElementsWithEventsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6586
        self.elementEventIds = {"type": "Vector.<uint>", "value": ""}
