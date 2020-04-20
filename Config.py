class Config:
    """ This classs represetas the configuration required for the connection"""

    host = "localhost"
    port = 4000
    time_out = 10

    def __repr__(self):
        return "Host  = " + self.host + "\n" \
            + "Port  = " + self.port + "\n" \
            + "time_out = ", self.time_out + "\n"
