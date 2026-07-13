import json
import os


def load_login_data():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "../data/login_data.json"
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)