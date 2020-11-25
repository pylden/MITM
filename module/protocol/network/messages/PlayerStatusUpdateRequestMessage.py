from module.protocol.network.message import Message


class PlayerStatusUpdateRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6455
        self.status = {"type": "PlayerStatus", "value": ""}
