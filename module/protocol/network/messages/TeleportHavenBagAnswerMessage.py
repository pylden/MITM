from module.protocol.network.message import Message


class TeleportHavenBagAnswerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7757
        self.accept = {"type": "Boolean", "value": ""}
