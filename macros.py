MACROS = {
    "OPEN_POWERSHELL": [
        "GUI r",
        "DELAY 200",
        "STRING powershell",
        "ENTER"
    ],
    "OPEN_CMD": [
        "GUI r",
        "DELAY 200",
        "STRING cmd",
        "ENTER"
    ],
    "OPEN_NOTEPAD": [
        "GUI r",
        "DELAY 200",
        "STRING notepad",
        "ENTER"
    ],
    "LOCK_SCREEN": [
        "GUI l"
    ],
    "OPEN_TASK_MANAGER": [
        "CTRL SHIFT ESC"
    ]
}

VALID_KEYS = {
    "ENTER", "ESC", "TAB",
    "UP", "DOWN", "LEFT", "RIGHT",
    "CTRL", "SHIFT", "ALT", "WINDOWS", "GUI", "SPACE", "BACKSPACE"
}

def expand_macros(line):
    line=line.strip()
    parts = line.split()

    if not parts:
        return [line]

    command = parts[0].upper()

    #Static macros
    if command in MACROS and len(parts) == 1:
        return MACROS[command]

    #for browsser
    if command == "OPEN_BROWSER" and len(parts) == 2:
        url = parts[1]
        if "." not in url:
            return["ERROR:Invalid url"]
        return [
            "GUI r",
            "DELAY 200",
            f"STRING https://{url}",
            "ENTER"
        ]

    #for app
    if command == "OPEN_APP" and len(parts) == 2:
        app = parts[1]
        return [
            "GUI r",
            "DELAY 200",
            f"STRING {app}",
            "ENTER"
        ]
    
    # WAIT <ms>
    if command == "WAIT" and len(parts) == 2:
        if parts[1].isdigit():
            return [f"DELAY {parts[1]}"]
        else:
            return["ERROR:Invalid delay value"]

    # TYPE <text>
    if command == "TYPE" and len(parts) >= 2:
        text = " ".join(parts[1:])
        return [f"STRING {text}"]

    # PRESS <key>
    if command == "PRESS" and len(parts) == 2:
        key = parts[1].upper()
        if key in VALID_KEYS:
            return[key]
        else:
            return [f"ERROR:Invalid key '{key}'"]
    
    return [line]