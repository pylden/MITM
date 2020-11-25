from module.protocol.network.message import Message


class JobExperienceOtherPlayerUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7414
        self.playerId = {"type": "Number", "value": ""}
