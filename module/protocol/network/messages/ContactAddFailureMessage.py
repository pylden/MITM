from module.protocol.network.message import Message


class ContactAddFailureMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2662
        self.reason = {"type": "uint", "value": ""}
