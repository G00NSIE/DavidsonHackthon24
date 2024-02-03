import json
import struct
import sys

# Open log file for writing messages
log_file = open("native_messaging_log.txt", "a")

def log_message(message):
    """Log messages to a file."""
    log_file.write(message + "\n")
    log_file.flush()

def send_message(message):
    """Send a message to the Chrome extension."""
    encoded_message = json.dumps(message).encode('utf-8')
    # First, send the length of the encoded message
    sys.stdout.buffer.write(struct.pack('=I', len(encoded_message)))
    # Then, send the message itself
    sys.stdout.buffer.write(encoded_message)
    sys.stdout.flush()

def receive_message():
    """Receive a message from the Chrome extension."""
    # Read the first 4 bytes of stdin, the message length (in little-endian format)
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        sys.exit(0)  # Exit if no input is received
    # Unpack the message length as a 32-bit unsigned int
    message_length = struct.unpack('=I', raw_length)[0]
    # Read the message of `message_length`
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

while True:
    try:
        received_message = receive_message()
        log_message(f"Received: {received_message}")  # Log received message
        # Example response - this can be customized
        response = {"received": "ok"}
        log_message(f"Sending: {response}")  # Log response message
        send_message(response)
    except Exception as e:
        # Log any exceptions to the log file and exit the loop
        log_message(f"Error: {str(e)}")
        break
