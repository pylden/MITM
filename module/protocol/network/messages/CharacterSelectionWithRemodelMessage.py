from module.protocol.network.message import Message


class CharacterSelectionWithRemodelMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5795
        self.remodel = {"type": "RemodelingInformation", "value": ""}
