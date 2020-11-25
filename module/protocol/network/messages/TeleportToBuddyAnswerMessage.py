from module.protocol.network.message import Message


class TeleportToBuddyAnswerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7626
        self.dungeonId = {"type": "uint", "value": ""}
        self.buddyId = {"type": "Number", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
