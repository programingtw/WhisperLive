from whisper_live.client import TranscriptionClient
client = TranscriptionClient("localhost", 9090, "Student")
client()