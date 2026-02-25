from macros import expand_macros

VALID_COMMANDS = [
    "REM", "DELAY", "STRING", "ENTER",
    "GUI", "CTRL", "SHIFT", "ALT",
    "TAB", "ESC","UP", "DOWN", "LEFT", "RIGHT"
]

def parse_script(input_text):
    lines = input_text.split("\n")
    final_script = []

    for idx, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue

        expanded_lines = expand_macros(line)

        for expanded in expanded_lines:
            #macro errors
            if expanded.startswith("ERROR"):
                return f"ERROR (Line {idx}): {expanded}"
            
            command = expanded.split(" ")[0]

            if command not in VALID_COMMANDS:
                return f"ERROR (Line {idx}): Invalid command '{command}'"

            final_script.append(expanded)

    return "\n".join(final_script)