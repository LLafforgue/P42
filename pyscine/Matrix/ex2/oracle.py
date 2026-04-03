import os
import sys
try:
    from dotenv import load_dotenv
except (ModuleNotFoundError) as e:
    print(e)
    print("\033[35m Install dotenv\033[0m :")
    print("\tpip install python-dotenv")


def check_dotenv(path: str) -> str:
    try:
        with open(path, 'r'):
            pass
        return path
    except (FileNotFoundError):
        print('')
    try:
        with open('.env', 'r'):
            pass
        return '.env'
    except (FileNotFoundError):
        print('No .env found')
        print('Use \033[4mcp .env.example .env\033[0m')

        sys.exit(1)


def set_path_basename(origin: str, base_target: str) -> str:
    ori_dir = '/'.join(origin.split('/')[:-1])
    if base_target[0] != '/':
        base_target = '/' + base_target
    return ori_dir + base_target


def test_env() -> int:
    invalid: int = 0

    if (os.environ.get('MATRIX_MODE')
        and
        os.environ.get('MATRIX_MODE').lower() in [
            'development',
            'production',
            'deployment']):
        print('Mode:', os.environ.get('MATRIX_MODE'))
    else:
        print('\033[1mError\033[0m Mode: Undefined')
        invalid += 1

    if os.environ.get('DATABASE_URL'):
        if os.environ.get('DATABASE_URL')[:4] in 'https':
            print('Database: Connected to local instance')
        else:
            print(('\033[31mAlert\033[0m',
                   'Database: Probably unreachable !'))
            invalid += 1
    else:
        print('Database: failed to connect')
        invalid += 1

    if os.environ.get('API_KEY'):
        print("API Access: Authenticated")
    else:
        print("API Access: failed")
        invalid += 1

    if os.environ.get('LOG_LEVEL'):
        print('Log Level:', os.environ.get('LOG_LEVEL'))
    else:
        print('Log Level: Not implemented')
        invalid += 1

    if os.environ.get('ZION_ENDPOINT'):
        if os.environ.get('ZION_ENDPOINT')[:4] in 'https':
            print('Zion Network: Online')
        else:
            print(('\033[31mAlert\033[0m',
                   'Zion Network: Probably unreachable !'))
            invalid += 1
    else:
        print('Zion Network: Deconnected')
        invalid += 1

    return invalid


def verif_Keys() -> str:
    try:
        with open(os_p.abspath(__file__), 'r') as fd:
            script = [w for w in fd.read().split(' ') if w != '']
            suspect: int = 0
            for w in script:
                if (
                    'APY_KEY=' in w
                    or 'DATABASE_URL=' in w or 'APY_KEY =' in w
                    or 'DATABASE_URL =' in w
                ):
                    suspect += 1
            if suspect > 2:
                return '[ALERT]: Secrets could be revealed!'
            return '[OK] No hardcoded secrets detected'
    except (Exception) as e:
        return e.args[0]


def overide_prod(path_env: str) -> str:
    env: str = ''
    over_log = os.environ['LOG_LEVEL']
    over_api = os.environ['API_KEY']
    with open(path_env, 'r') as f:
        env = f.read()
    if over_log not in env or over_api not in env:
        return '[OK] Production overrides available'
    else:
        return ("[KO] Test "
                + "'MATRIX_MODE=production LOG_LEVEL=TRUE"
                + " python3 oracle.py'"
                )


if __name__ == "__main__":
    print('ORACLE STATUS: Reading the Matrix...\n')
    os_p = os.path
    path_env = set_path_basename(os_p.abspath(__file__),
                                 '.env')
    path_env = check_dotenv(path_env)
    if load_dotenv():
        print('Configuration loaded:')
        invalid_num = test_env()
        print('\nEnvironment security check:')
        print(verif_Keys())
        print(('[OK] .env file properly configured'
               if invalid_num == 0
               else '[ALERT]: .env could be badly configured!'
               ))
        print(overide_prod(path_env))
    else:
        print('error in loading')

    print('\nThe Oracle sees all configurations.')
