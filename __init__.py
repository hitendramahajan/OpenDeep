import os
import sys
import logging
import subprocess


def collect_py_files(root_folder_path, env_path, env_type, excludes):
    py_files = []
    for root, dirs, files in os.walk(root_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if (
                file.endswith(".py")
                and __file__ not in file_path
                and file_path not in EXCLUDE_FILES
                and env_path not in  file_path
                ):
                if env_type == "Pipenv":
                    py_files.append(file_path)
                elif env_path not in file_path :
                    py_files.append(file_path)
 
    return py_files


def run_without_debugging(py_files, log_file, target_venv_executable):
    for py_file in py_files:
        # Use the target folder's virtual environment if available
        if target_venv_executable:
            process = subprocess.Popen([target_venv_executable, py_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            process = subprocess.Popen([sys.executable, py_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout_output, stderr_output = process.communicate()
        if stderr_output:
            logging.error("Error in {}: {}".format(py_file, stderr_output.decode('utf-8')))

    with open(log_file, 'r') as fp:
        if 'ERROR:root:' not in fp.read():
            logging.info("Successfully executed : Done!")
        else:
            logging.info("\nDone!")

def main():
    py_files = collect_py_files(PATH, VENV_PATH, ENV_TYPE, EXCLUDE_FILES)
    run_without_debugging(py_files, LOG_FILE, INTERPRETER_PATH)


if __name__ == '__main__':
    PATH = r'e:\IDE\OpenDeep'

    EXCLUDE_FILES = [__file__]

    INTERPRETER_PATH = r'e:\IDE\OpenDeep\venv\Scripts\python.exe'

    VENV_PATH = r'e:\IDE\OpenDeep\venv'

    ENV_TYPE = r'Python venv'

    LOG_FILE = r'c:\Users\Administrator\.vscode\extensions\undefined_publisher.sasva-toolkit-0.2.4\Config\error_log.txt'

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, filemode='w')

    main()
