from module.protocol.network.message import Message


class GameFightResumeWithSlavesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1238
        self.slavesInfo = {"type": "Vector.<GameFightResumeSlaveInfo>", "value": ""}
