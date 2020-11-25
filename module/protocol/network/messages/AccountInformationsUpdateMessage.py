from module.protocol.network.message import Message


class AccountInformationsUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4873
        self.subscriptionEndDate = {"type": "Number", "value": ""}
