import allure
from datetime import datetime

class StepLogger:
    def __init__(self):
        self.counter = 1

    def log(self, message: str):
        now = datetime.now().strftime("%H:%M:%S")
        step_message = f"Step {self.counter}: {message}"
        full_message = f"{now} {step_message}"
        print(full_message)
        allure.attach(body=full_message, name=step_message, attachment_type=allure.attachment_type.TEXT)
        self.counter += 1