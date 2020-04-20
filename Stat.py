class Stats:
    "This Object gives snapshot of clinet and server statistics"
    messageIn = 0
    messageOut = 0
    bytesIn = 0
    bytesOut = 0
    timeout = 0

    def __repr__(self):
        return "Messages in :" + str(self.messageIn) + "\n"  \
            + "Messages out : " + str(self.messageOut) + "\n" \
            + "Bytes In :" + str(self.bytesIn) + "\n" \
            + "Bytes Out :" + str(self.bytesOut) + "\n" \
            + "Timeout :" + str(self.timeout)
