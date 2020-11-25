from module.protocol.network.message import Message


class ContactLookRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4354
        self.requestId = {"type": "uint", "value": ""}
        self.contactType = {"type": "uint", "value": ""}
