from pathlib import Path

try:
    file = open('my_file.py')
except FileNotFoundError as exc:
    print('Arquivo não encontrado')
    print(exc)
except IOError as exc:
    print(f'Erro ao abrir: {exc}')
except Exception as exc:
    print(f'Algum erro ocorreu {exc}')

ROOT_PATH = Path(__file__).parent

try:
    file = open(ROOT_PATH / 'new_dir')
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f'Erro ao abrir: {exc}')
except Exception as exc:
    print(f'Algum erro ocorreu {exc}')