from module.protocol.network.message import Message


class EvolutiveObjectRecycleResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6221
        self.recycledItems = {"type": "Vector.<RecycledItem>", "value": ""}
