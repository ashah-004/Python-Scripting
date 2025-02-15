import os
import json 
import shutil
from subprocess import PIPE, run
import sys

GAME_PATH_PATTERN = "game"
GAME_CODE_EXT = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_PATH_PATTERN in directory.lower():
                game_path = os.path.join(source, directory)
                game_paths.append(game_path)
        
        break

    return game_paths


def fetch_name_from_paths(paths, to_remove):
    new_names = []

    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_remove, "")
        new_names.append(new_dir_name)

    return new_names


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)

def copy_and_overwrite(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(source, destination)

def make_json_metadata_file(path, game_dirs):
    data = {
        "game_names" : game_dirs,
        "number_of_games" : len(game_dirs)
    }

    with open(path, 'w') as f:
        json.dump(data, f)


def run_command(command, path):
    cwd = os.getcwd()

    os.chdir(path)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print("compile result", result)

    os.chdir(cwd)


def compile_game(path):
    code_file_name = None

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXT):
                code_file_name = file
                break
        break

    if code_file_name == None:
        return
    
    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)


def main (source, destination):
    # getting the current directory that we run this script from
    cwd = os.getcwd()
 
    # joining the path with the source and destination locations we want to use to get the full path
    source_path = os.path.join(cwd, source)
    destination_path = os.path.join(cwd, destination)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = fetch_name_from_paths(game_paths, "_game")

    create_directory(destination_path)

    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(destination_path, dest)
        copy_and_overwrite(src, dest_path)
        compile_game(dest_path)

    json_path = os.path.join(destination_path, "metadata.json")
    make_json_metadata_file(json_path, new_game_dirs)


if  __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("you must pass a source and target directory - only.")
    
    source, destination = args[1:]
    main(source, destination)

