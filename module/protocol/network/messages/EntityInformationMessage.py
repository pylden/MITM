from module.protocol.network.message import Message


class EntityInformationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7068
        self.entity = {"type": "EntityInformation", "value": ""}
