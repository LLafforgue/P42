import sys
import site
import os

os_p = os.path


def n_basename(path: str, n: int) -> str:
    if n == 0:
        return ''
    return (n_basename(os_p.dirname(path), n - 1)
            + "/" + os_p.basename(path))


def print_venv_info(prefix: str) -> None:
    """Print infos related to venv activation."""
    print("\033[35mMATRIX STATUS:\033[0m Welcome to the construct")
    print("\nCurrent Python :",  ("/path/to" + n_basename(sys.executable, 3)))
    print(f"Virtual Environment: {os_p.basename(prefix)}")
    print("Environment Path:", ("/path/to/" + os_p.basename(prefix)))
    print("\n\033[35mSUCCESS\033[0m: You're in an isolated environment !")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path:")
    print("/path/to" + n_basename(site.getsitepackages()[-1], 4))
    print('Use \033[1mdeactivate\033[0m to desactivate the matrix.')


def print_norm_info(path: str) -> None:
    """Print infos when venv is not activate"""
    print("\033[33mMATRIX STATUS:\033[0m You`re still plugged in")
    print("\nCurrent Python :",  path)
    print(("\n\033[31mWARNING:\033[0m You're in the global environment!"
           + "\nThe machines can see everything you install.\n"))
    print(("--To enter the construct--" +
           "\n\033[1mpython -m venv matrix_env\033[0m" +
           "\n\033[1msource matrix_env/bin/activate\033[0m " +
           " \033[30m# On Unix\033[0m" +
           "\nmatrix_env" +
           "\nScripts" +
           "\nactivate \033[30m# On Windows\033[0m" +
           "\nThen run this program again."))


def execute_venv() -> None:
    try:
        start = os.getcwd()
        print(start)
        while start != '/':
            for dir in os.walk(start):
                if (start + '/matrix_env') in dir:
                    print("\033[35m'matrix_env'\033[0m located.")
                    if (input(
                             'Would you like to activate it ? [y/n]'
                             ).lower() == 'y'):
                        os.system(
                            f"bash --rcfile {start}/matrix_env/bin/activate")
                    sys.exit()
            start = os_p.dirname(start)
    except OSError as e:
        print(e)


if __name__ == "__main__":
    prefix = sys.prefix
    path = sys.executable
    test = prefix != sys.base_prefix
    if test:
        print_venv_info(prefix)
    else:
        print_norm_info(path)
        execute_venv()
