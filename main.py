from __future__ import annotations

import platform
import subprocess
import json
import os

with open(os.path.join("settings", "commands.json"), "r") as f:
    settings: dict = json.load(f)


class AutoScript:
    def __init__(self):
        pass

    def get_system(self) -> str:
        match platform.system():
            case "Linux":
                return str(platform.freedesktop_os_release().get("ID_LIKE"))
            case _:
                raise EnvironmentError("Your system is not supported by this script")

    def script_execute(self) -> None:
        for package in settings["linux"][self.get_system().upper()]:
            subprocess.run(package.split(), check=True)
        else:
            raise EnvironmentError("Distribution not supported by this script")


if __name__ == "__main__":
    auto = AutoScript()
    auto.script_execute()
