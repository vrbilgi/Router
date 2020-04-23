import struct
import sys
import json


class Message:
    """
    Message = Fixed_len_header_2byte + varible_len_json_header + \
              variable_len_content
    """
    def __init__(self):
        self.message_hdr = None
        self.content_bytes = None
        self.jsonheader_bytes = None
        self.content_encoding = ["utf-8", "binary"]
        self.content_type = ["text/json", "binary/custom-server-binary-type"]

    def _json_encode(self, obj, encoding):
        return json.dumps(obj, ensure_ascii=False).encode(encoding)

    def encode_message(self, content):
        jsonheader = {
            "byteorder": sys.byteorder,
            "content-type": self.content_type[0],
            "content-encoding": self.content_encoding[0],
            "content-length": len(content),
        }
        jsonheader_bytes = self._json_encode(jsonheader, "utf-8")
        message_hdr = struct.pack(">H", len(jsonheader_bytes))
        message = message_hdr + jsonheader_bytes + content
        return message

    def decode_message(self, content):
        hdrlen = 2
        if len(content) >= hdrlen:
            self._jsonheader_len = struct.unpack(
                ">H", content[:hdrlen]
            )[0]
            content = content[hdrlen:]
            return content
