from macros import expand_macros

VALID_COMMANDS = [
    "REM", "DELAY", "STRING", "ENTER",
    "GUI", "CTRL", "SHIFT", "ALT", "ESC"
]

def parse_script(input_text):
    lines = input_text.split("\n")
    final_script = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        expanded_lines = expand_macros(line)

        for expanded in expanded_lines:
            command = expanded.split(" ")[0]

            if command not in VALID_COMMANDS:
                return f"Error: Invalid command '{command}'"

            final_script.append(expanded)

    return "\n".join(final_script)