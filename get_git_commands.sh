#!/bin/bash

# Get the shell history file (adjust for your shell if necessary)
history | grep -E '\bgit\b' | awk '{$1=""; print $0}' | sort > git_commands.txt
echo "Git commands written to git_commands.txt"

