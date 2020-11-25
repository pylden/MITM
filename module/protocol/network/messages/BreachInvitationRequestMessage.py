from module.protocol.network.message import Message


class BreachInvitationRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 19
        self.guests = {"type": "Vector.<Number>", "value": ""}
