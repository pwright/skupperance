import os
import subprocess
import re
import markdown
import time

BASE_COMMAND = "skupper"
OUTPUT_DIR = "docs"


def run_command(command):
    """Run a CLI command and return its output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running command {command}: {e}", file=sys.stderr)
        return None


def extract_commands(help_text):
    """Extract available subcommands from the help text."""
    commands = []
    in_section = False
    for line in help_text.split("\n"):
        line = line.strip()
        if line.startswith("Available Commands:") or line.startswith("Commands:"):
            in_section = True
            continue
        if in_section:
            match = re.match(r"^(\S+)", line)
            if match:
                commands.append(match.group(1))
            elif not line:  # Stop if we hit an empty line
                break
    return commands


def write_markdown(command_path, help_text):
    """Write the help text as a Markdown file."""
    filename = command_path.replace(" ", "_") + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# `{command_path}` Command Reference\n\n")
        f.write(f"```\n{help_text}\n```\n")


def process_command(command_path, visited):
    """Recursively process a command and its subcommands."""
    if command_path in visited:
        return  # Avoid redundant calls

    visited.add(command_path)
    
    command_str = f"{command_path} -h"
    help_text = run_command(command_str)

    if not help_text:
        print(f"Skipping {command_str} due to empty output", file=sys.stderr)
        return

    write_markdown(command_path, help_text)
    subcommands = extract_commands(help_text)

    for subcommand in subcommands:
        new_command_path = f"{command_path} {subcommand}"
        process_command(new_command_path, visited)


def main():
    visited = set()
    process_command(BASE_COMMAND, visited)
    print(f"Documentation saved in `{OUTPUT_DIR}/`")


if __name__ == "__main__":
    main()
