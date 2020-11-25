from module.protocol.network.message import Message


class AlliancePrismDialogQuestionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7491
