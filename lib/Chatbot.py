import os
import aiml
import logging
import re


class Chatbot:
    BRAIN_FILE = "brain.dump"

    def __init__(self):

        self.exit_regex = re.compile(
            r"^(quit|by|byee|bye|close|end|exit)$", re.IGNORECASE)
        self.kernel = aiml.Kernel()

        # Load the brain file
        if os.path.exists(os.environ["BRAIN_FILE"]):
            logging.info(f"Loading from brain file: " +
                         os.environ["BRAIN_FILE"])
            self.kernel.loadBrain(os.environ["BRAIN_FILE"])
        else:
            logging.info("Parsing aiml files")
            self.kernel.bootstrap(
                learnFiles="std-startup.aiml", commands="load aiml b")
            logging.info("Saving brain file: " + os.environ["BRAIN_FILE"])
            self.kernel.saveBrain(os.environ["BRAIN_FILE"])

    def respond(self, message: str) -> str:
        match = self.exit_regex.match(message)

        if match:
            return "Thank you! See you later."

        return self.kernel.respond(message)

    def close(self):
        if os.environ["MODE"] == "DEVELOPMENT":
            try:
                os.remove(os.environ["BRAIN_FILE"])
            except:
                print("Failed to delete the brain dump file")
