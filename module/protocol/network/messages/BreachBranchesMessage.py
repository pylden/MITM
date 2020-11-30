from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachBranchesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1352
        self.branches = {"type": "Vector.<ExtendedBreachBranch>", "value": ""}
