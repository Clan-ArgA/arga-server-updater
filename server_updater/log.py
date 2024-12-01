class Log:
    @staticmethod
    def log_title(msg: str) -> None:
        log_output = f"\n{'':=<{len(msg)}}\n{msg}\n{'':=<{len(msg)}}"
        print(log_output, flush=True)

    def log(self, msg: str | None = "") -> None:
        print(msg, flush=True)
