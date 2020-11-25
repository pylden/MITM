from module.protocol.network.message import Message


class GameActionFightDispellEffectMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 827
        self.boostUID = {"type": "uint", "value": ""}
