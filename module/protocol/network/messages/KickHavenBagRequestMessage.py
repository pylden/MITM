from module.protocol.network.message import Message


class KickHavenBagRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 711
        self.guestId = {"type": "Number", "value": ""}
