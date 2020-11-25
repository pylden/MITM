from module.protocol.network.message import Message


class EvolutiveObjectRecycleResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6221
        self.recycledItems = {"type": "Vector.<RecycledItem>", "value": ""}
