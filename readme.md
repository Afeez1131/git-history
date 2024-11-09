# Git Command History Analyzer

## Overview

This project contains a **Bash + Python** script that extracts and analyzes your Git command history from your terminal. The goal is to help **beginners** and **Git learners** see the most commonly used commands in real-world development workflows.

You can find my own history from in the file `sample_processed_git_commands.txt'

## Key Features

- **Command Extraction:** Extracts all Git commands from your terminal history using **Bash**.
- **Data Analysis:** The **Python** script analyzes these commands, counting how often each one is used.

## Prerequisites

Before running this script, ensure you have the following installed:

- **Bash** – Commonly pre-installed on Linux and macOS.
- **Python 3.x** – [Download Python](https://www.python.org/downloads/) if you don't have it installed.

## Running the Script

### 1. Clone the Repository

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/git-history.git
   cd git-history
   ```

### 2. Extract Git Commands

   On your terminal, run the following command to extract all Git commands from your terminal history:

   ```bash
   history | grep -E '\bgit\b' | awk '{$1=""; print $0}' | sort > git_commands.txt
   ```

   This will create a file called `git_commands.txt` containing all your Git commands.

### 3. Analyze the Commands

   Run the Python script to analyze the extracted Git commands:

   ```bash
   python process_history.py
   ```

   The script will process the `git_commands.txt` file and generate insights, outputting the results to a new file called `processed_git_commands.txt`.

## Key Insights

- The analysis will show you the most commonly used Git commands in your history.
- It will also display the frequency of each command.

## Contributing

Feel free to **fork** the repository, submit **pull requests**, or open **issues** for bugs or feature requests. Your contributions are always welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

## TODO
- Generating response as HTML output, then visualize the data with charts/graphs.
