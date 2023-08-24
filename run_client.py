from whisper_live.client import TranscriptionClient
client = TranscriptionClient("140.121.17.72", 8080, True, "zh", False)
client()