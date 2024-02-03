import json
import struct
import sys

print("heres a response for ya")

log_file = open("native_messaging_log.txt", "a")

def log_message(message):
    log_file.write(message + "\n")
    log_file.flush()

def send_message(message):
    encoded_message = json.dumps(message).encode('utf-8')
    sys.stdout.buffer.write(struct.pack('I', len(encoded_message)))
    sys.stdout.buffer.write(encoded_message)
    sys.stdout.flush()

def receive_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        sys.exit(0)
    message_length = struct.unpack('I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

while True:
    received_message = receive_message()
    log_message(f"Received: {received_message}")  # Log received message
    response = {"received": received_message}
    log_message(f"Sending: {response}")  # Log response message
    send_message(response)

