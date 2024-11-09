import re
import describe_command

# Input and output file paths
input_file = "git_commands.txt"
output_file = "processed_git_commands.txt"

# Read the Git commands from the input file
with open(input_file, "r") as file:
    git_commands = file.readlines()

# Function to remove duplicate and describe Git commands
def process_git_commands(commands):
    command_counts = {}  # Dictionary to store command counts
    described_commands = []  # List to store the described commands

    for command in commands:
        # Remove leading/trailing whitespace and newline characters
        command = command.strip()

        # Describe the command based on the subcommand
        described_command = describe_command.describe_command(command)

        # Increment the count for the described command in the dictionary
        if described_command in command_counts:
            command_counts[described_command] += 1
        else:
            command_counts[described_command] = 1

    # Generate the list of unique commands with their counts
    for command, count in command_counts.items():
        described_commands.append(f"{command} (Used {count} times)")

    return described_commands

# Process the Git commands
unique_git_commands = process_git_commands(git_commands)

# Write the unique, described commands and their counts to the output file
with open(output_file, "w") as file:
    file.write("Unique Git commands used:\n")
    for command in unique_git_commands:
        file.write("- " + command + "\n")

print(f"Processed Git commands written to {output_file}")
