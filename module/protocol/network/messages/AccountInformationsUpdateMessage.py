from module.protocol.network.message import Message


class AccountInformationsUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4873
        self.subscriptionEndDate = {"type": "Number", "value": ""}
