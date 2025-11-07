import os
import sys
import time
import re
from math import pi

# константи
DATA_FILE = "data.txt"
CONFIG_DEFAULT = "config.ini"
GLOBLFLAG = True
TEMP = None
A = list(range(1, 11))  # виправила формат списку
B = list(range(1, 11))  # виправила формат списку


def do_thing(x, y, z=None):
    # Виправила mutable default, зрозуміла назва
    if z is None:
        z = []
    z.extend([x, y])
    return [i * i for i in z if i > 2]  # залишила логіку, тільки пробіли поправила


def calc_sum(lst):
    # Виправила дублікати calcSum/CalcSUM, зробила одну функці
    return sum(lst)


def parse_config(cfg_path):
    # Виправила bare except, назву функції змінила
    config = {}
    try:
        with open(cfg_path, 'r', encoding='utf-8') as f:  # використала with
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key.strip()] = value.strip()
    except FileNotFoundError:  # конкретний except
        return None
    return config


def format_user(user):
    # Виправила пробіли, зробила читабельніше
    return f"{user.get('Name', '')} - age:{user.get('age', '')} - city: {user.get('City', '')}"


def main():
    global TEMP
    cfg_path = sys.argv[1] if len(sys.argv) > 1 else CONFIG_DEFAULT

    # виклики функцій, прибрала дублікати
    x = do_thing(1, 2)
    y = do_thing(3, 4)
    z = do_thing(5, 6)

    big_list = A + B + list(range(11, 16))
    total_sum = calc_sum(big_list)

    if GLOBLFLAG:
        TEMP = total_sum * 4  # замість s1+s2+s3+s4 дублікати прибрала
    else:
        TEMP = None

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            raw = f.read()
    except FileNotFoundError:
        raw = "1,2,3,4,5,6,7,8,9,10"  #пробіли прибрала

    pattern = re.compile(r'\s+')
    arr = [int(pattern.sub('', q)) for q in raw.split(',') if q.strip()]  # прибрала дублікати

    arr.sort()  # замінила два сортування на одне

    # юзери
    users = [
        {'Name': 'Ivan', 'age': 30, 'City': 'Kyiv'},
        {'Name': 'Olga', 'age': 25},
        {'Name': 'Stepan', 'age': 41, 'City': 'Lviv'}
    ]
    res = [format_user(u) for u in users]  # замість двох циклів

    cfg_map = parse_config(cfg_path)
    if cfg_map is None:
        print("Config file is missing or invalid. Using defaults.")
        cfg_map = {'mode': 'x', 'retry': '3', 'debug': 'false'}

    mode = cfg_map.get('mode', 'x')
    if mode in ('x', 'y', 'z'):  # прибрала повтори
        print(f"MODE: {mode}")
        print(f"TEMP: {TEMP}")
        print(f"LEN: {len(arr)}")
    else:
        print("UNKNOWN MODE")

    # фінальний вивід
    print(
        "Final:", TEMP,
        "| arr =", arr,
        "| x,y,z =", x, y, z,
        "| res =", res,
        "| cwd =", os.getcwd(),
        "| time =", time.time(),
        "| pi =", pi,
        "| cfgpath =", cfg_path,
        "| data path =", DATA_FILE
    )


if __name__ == '__main__':
    main()
