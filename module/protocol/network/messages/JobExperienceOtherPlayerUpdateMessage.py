from module.protocol.network.message import Message


class JobExperienceOtherPlayerUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7414
        self.playerId = {"type": "Number", "value": ""}
