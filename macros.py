def expand_macros(line):
    if line == "OPEN_POWERSHELL":
        return [
            "GUI r",
            "DELAY 200",
            "STRING powershell",
            "ENTER"
        ]
    return [line]