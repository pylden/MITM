from module.protocol.network.message import Message


class AcquaintanceSearchErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3119
        self.reason = {"type": "uint", "value": ""}
