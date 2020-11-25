from module.protocol.network.message import Message


class EnterHavenBagRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2716
        self.havenBagOwner = {"type": "Number", "value": ""}
