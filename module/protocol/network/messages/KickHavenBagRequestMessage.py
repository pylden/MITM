from module.protocol.network.message import Message


class KickHavenBagRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 711
        self.guestId = {"type": "Number", "value": ""}
