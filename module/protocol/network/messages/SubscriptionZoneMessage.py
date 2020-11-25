from module.protocol.network.message import Message


class SubscriptionZoneMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9729
        self.active = {"type": "Boolean", "value": ""}
