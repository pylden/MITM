from module.protocol.network.message import Message


class SubscriptionZoneMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9729
        self.active = {"type": "Boolean", "value": ""}
