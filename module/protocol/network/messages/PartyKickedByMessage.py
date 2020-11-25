from module.protocol.network.message import Message


class PartyKickedByMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2914
        self.kickerId = {"type": "Number", "value": ""}
