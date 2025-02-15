# Python Scripting Project

This project demonstrates various tasks achievable through Python scripting. It covers automating processes related to managing game directories, compiling and running game code, and generating a summary of the games in a structured format.

## Assumptions

- The project works with a large data directory containing numerous files and subdirectories.
- The primary focus is on directories related to games, though the script can be easily adapted for other use cases with minimal modifications.
- Each game directory contains the word "game" in its name.
- Inside each game directory, there is a single `.go` file that needs to be compiled before execution.

## Project Workflow

1. **Identify Game Directories**: Traverse the `/data` directory to find all directories related to games.
2. **Create `/new-games` Directory**: Set up a new `/new-games` directory where the games will be organized.
3. **Organize and Copy Game Files**: Copy the game directories into `/new-games`, removing the "game" suffix from the directory names.
4. **Generate Metadata File**: Create a `.json` file that contains information about the games.
5. **Compile Game Code**: Compile all `.go` files in the game directories.
6. **Run Game Code**: Execute the compiled game code.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/ashah-004/Python-Scripting.git
   cd Pyhton-Scripting

2. Run the script to begin the automation process:
   ```bash
   python3 fetch_games.py

3. After running the script, check the /new_games directory for organized game files and the generated .json metadata.

## Requirements

- **Python 3.x**: Make sure Python 3 is installed on your machine.
- **Go Compiler**: Required for compiling the `.go` files. Make sure the Go compiler is installed and set up on your system.

