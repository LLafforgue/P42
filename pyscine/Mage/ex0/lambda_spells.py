#!/usr/bin/env python3
import sys
try:
    import data_generator as gen
except ModuleNotFoundError:
    print("\033[35m\033[1mYou need 'data_generator.py'.\033[0m")
    sys.exit(1)


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort."""
    try:
        return sorted(artifacts, key=lambda x: x['power'], reverse=True)
    except KeyError as e:
        print(e)
        return artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter."""
    try:
        fltr_mage = filter(lambda x: x['power'] >= min_power, mages)
        return list(fltr_mage)
    except KeyError as e:
        print(e)
        return mages


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda x: '* ' + str(x) + ' *', spells))
    except Exception as e:
        print(e)
        return spells


def mage_stats(mages: list[dict]) -> dict:
    try:
        if len(mages) == 1:
            s_max = mages[0]['power']
            s_min = s_max
            s_avg = s_max
        else:
            s_max = max(*mages, key=lambda x: x['power'])['power']
            s_min = min(*mages, key=lambda x: x['power'])['power']
            s_avg = sum(list(map(lambda x: x['power'], mages))) / len(mages)
        return {
            'max_power': s_max,
            'min_power': s_min,
            'avg_power': round(s_avg, 2)
        }
    except (KeyError, ValueError) as e:
        print(e)
        return {'data': 'error'}


if __name__ == "__main__":
    try:
        list_size = int(input('How many datas do you want to test ? '))
        if list_size <= 0:
            raise ValueError
    except (ValueError):
        print('Choose a number > 0 next time !')
        sys.exit(1)
    min_power = 75
    data_art = gen.FuncMageDataGenerator.generate_artifacts(list_size)
    data_mag = gen.FuncMageDataGenerator.generate_mages(list_size)
    data_spells = gen.FuncMageDataGenerator.generate_spells(list_size)
    data_spells_p = gen.FuncMageDataGenerator.generate_spell_powers(list_size)
    sorted_data = artifact_sorter(data_art)
    fltr_mage = power_filter(data_mag, min_power)
    trans_spells = spell_transformer(data_spells)
    stat_spells = mage_stats([{'name': k, 'power': p}
                              for k, p in zip(data_spells, data_spells_p)])
    if list_size < 6:
        try:
            print("\033[4m\nTesting artifact sorter...\033[0m\n",
                  "\n ".join([f'- {a['name']} power: {a['power']}'
                             for a in sorted_data]))
            print(f"\n\033[4mTesting power filter (>= {min_power}) ...",
                  "\033[0m\n -",
                  '\n - '.join([
                      f'{a['name']} power: {a['power']}'for a in fltr_mage]))
            print("\n\033[4mTesting spell transformer...\n\033[0m",
                  "\n ".join(trans_spells))
            print("\n\033[4mTesting spell transformer...\n\033[0m",
                  "\n ".join([f'{s}: {n}' for s, n in stat_spells.items()])
                  )
        except KeyError as e:
            print(e)
    else:
        print("\n========== Short demonstration ==========\n")
        print("\033[33m\033[1mTesting artifact sorter...\033[0m")
        print(f'{sorted_data[0]['name']} ({sorted_data[0]['power']} power) '
              + f'comes before {sorted_data[1]['name']} '
              + f'({sorted_data[1]['power']} power)...')
        print(f"\n\033[36m\033[1mTesting power filter (>= {min_power})"
              + "...\033[0m")
        print(f"Initial nbr of mages less powerfull than {min_power} power: "
              + f"\033[4m{sum(1 for _ in data_mag if _['power'] < min_power)}"
              + "\033[0m\n--> After filter : \033[4m"
              + f"{sum(1 for _ in fltr_mage if _['power'] < min_power)}\033[0m"
              )
        print("\n\033[33m\033[1mTesting spell transformer...\033[0m")
        print(f"Transformation example : {data_spells[0]} "
              + f"--> {trans_spells[0]}")

        print("\n\033[36m\033[1mTesting mage stats...\033[0m\n",
              "\n ".join([f'{s}: {n}' for s, n in stat_spells.items()])
              )
