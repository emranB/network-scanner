import os, logging

class Logger:
    def __init__(self, log_config, root_path):
        self.config     = log_config
        self.root_path  = root_path

        log_to_screen   = self.config.get("log_to_screen", False)
        log_to_file     = self.config.get("log_to_file", False)
        log_file        = self.config.get("log_file", "scanner.log")
        self.debug      = self.config.get("debug", False)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if log_to_screen:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        if log_to_file:
            file_handler = logging.FileHandler(os.path.join(self.root_path, log_file))
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def info(self, message):
        if self.debug: print(message)
        self.logger.info(message)

    def error(self, message):
        if self.debug: print(message)
        self.logger.error(message)
