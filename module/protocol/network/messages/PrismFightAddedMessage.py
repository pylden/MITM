from module.protocol.network.message import Message


class PrismFightAddedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9780
        self.fight = {"type": "PrismFightersInformation", "value": ""}
