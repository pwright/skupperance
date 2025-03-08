import os
import subprocess
import re

BASE_COMMAND = "skupper"
PLATFORMS = ["kubernetes", "podman"]
OUTPUT_DIR = "docs"


def run_command(command):
    """Run a CLI command and return its output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
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


def write_markdown(platform, command_path, help_text, subcommands):
    """Write the help text as a Markdown file and include links to subcommands."""
    platform_dir = os.path.join(OUTPUT_DIR, platform)
    os.makedirs(platform_dir, exist_ok=True)

    filename = command_path.replace(" ", "_") + ".md"
    filepath = os.path.join(platform_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# `{command_path}` Command Reference ({platform})\n\n")
        f.write(f"```\n{help_text}\n```\n")

        if subcommands:
            f.write("\n## Subcommands\n")
            for sub in subcommands:
                sub_filename = f"{command_path.replace(' ', '_')}_{sub}.md"
                f.write(f"- [{sub}](./{sub_filename})\n")


def process_command(platform, command_path, visited):
    """Recursively process a command for a given platform and its subcommands."""
    if (platform, command_path) in visited:
        return  # Avoid redundant calls

    visited.add((platform, command_path))

    command_str = f"{command_path} -p {platform} -h"
    help_text = run_command(command_str)

    if not help_text:
        print(f"Skipping {command_str} due to empty output", file=sys.stderr)
        return

    # Extract subcommands and generate markdown
    subcommands = extract_commands(help_text)
    write_markdown(platform, command_path, help_text, subcommands)

    # Recursively process each subcommand
    for subcommand in subcommands:
        new_command_path = f"{command_path} {subcommand}"
        process_command(platform, new_command_path, visited)


def main():
    visited = set()
    for platform in PLATFORMS:
        print(f"Processing documentation for platform: {platform}")
        process_command(platform, BASE_COMMAND, visited)

    print(f"Documentation saved in `{OUTPUT_DIR}/` under platform-specific directories.")


if __name__ == "__main__":
    main()
