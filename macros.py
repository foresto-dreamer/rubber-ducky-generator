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

def expand_macros(line):
    return MACROS.get(line, [line])