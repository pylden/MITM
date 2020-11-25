from module.protocol.network.message import Message


class BreachBranchesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1352
        self.branches = {"type": "Vector.<ExtendedBreachBranch>", "value": ""}
