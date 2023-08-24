from whisper_live.server import TranscriptionServer

if __name__ == "__main__":
    server = TranscriptionServer()
    server.run("140.121.17.72", 9090)
