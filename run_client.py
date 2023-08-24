from whisper_live.client import TranscriptionClient
client = TranscriptionClient("140.121.17.72", 9090, True, "zh", False)
client()

