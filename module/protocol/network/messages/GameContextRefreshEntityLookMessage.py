from module.protocol.network.message import Message


class GameContextRefreshEntityLookMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5695
        self.id = {"type": "Number", "value": ""}
        self.look = {"type": "EntityLook", "value": ""}
