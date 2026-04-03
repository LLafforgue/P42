import sys
import importlib

REQUIRED: dict = {
    'pandas': '2.1.0',
    'requests': '2.31.0',
    'matplotlib': '3.7.2'
}


def version(v: str) -> tuple:
    return tuple(map(int, v.split(".")))


def test_imports() -> list:
    modules: list = []
    for pkg, vers in REQUIRED.items():
        try:
            module = importlib.import_module(pkg)
            modules.append(module)
            if version(vers) > version(module.__version__):
                print(
                    f"[ERROR] {pkg} version mismatch "
                    f"(installed={module.__version__}, required={vers})"
                )
                sys.exit(1)
        except (AttributeError, ModuleNotFoundError, ValueError) as e:
            print(e)
            print(
                'Use in shell \033[33mpip install -r requirements.txt\033[0m'
                + '\nor\n'
                + '\033[33mUse Poetry:\n\033[0m'
                + 'poetry install\n'
                + '[hors matrix_env] :'
                + ' poetry python run loading.py'
                + '\n[dans matrix_env] : py loadin.py')
            sys.exit(1)
    return modules


def test_venv() -> None:
    if sys.prefix == sys.base_prefix:
        print('\033[31mWarning: you should be in the Matrix.\033[0m')
        print(("--To enter the construct--" +
              "\n\033[1mpython -m venv matrix_env\033[0m" +
               "\n\033[1msource matrix_env/bin/activate\033[0m " +
               " \033[30m# On Unix\033[0m" +
               "\nmatrix_env" +
               "\nScripts" +
               "\nactivate \033[30m# On Windows\033[0m" +
               "\nThen run this program again."))
        sys.exit(1)


def test_request(modules: list) -> None:
    import matplotlib.pyplot as plt

    pokemons = ["bulbasaur", "charmander", "squirtle"]

    rows = []
    pd = modules[0]
    requests = modules[1]

    for p in pokemons:
        data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{p}").json()

        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        stats["name"] = p

        rows.append(stats)

    df = pd.DataFrame(rows)
    print(df)

    first_pokemon = df.iloc[0]
    names = df.columns.drop("name")
    values = first_pokemon[names].values

    plt.bar(names, values)
    plt.title(first_pokemon["name"])
    plt.ylabel("stat value")
    plt.show()


if __name__ == "__main__":
    test_venv()
    modules = test_imports()
    print(("Checking dependencies:\n"
           + "[OK] pandas (2.1.0) - Data manipulation ready\n"
           + "[OK] requests (2.31.0) - Network access ready\n"
           + "[OK] matplotlib (3.7.2) - Visualization ready"))
    test_request(modules)
