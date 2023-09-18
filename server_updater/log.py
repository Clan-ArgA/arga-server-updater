class Log:
    @staticmethod
    def log(msg: str) -> None:
        log_output = f"\n{'':=<{len(msg)}}\n{msg}\n{'':=<{len(msg)}}"
        print(log_output, flush=True)
