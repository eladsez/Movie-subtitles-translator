from googletrans import Translator
from tqdm import tqdm


def read_lines(file_path: str) -> list:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    return lines


def write_lines(list_of_lines: list):
    pass


def split_to_threads(lines: list):
    pass




def srt_tran(lines: str, language: str) -> list:
    translator = Translator()

    trans_lines = []


    index = 0
    tran = False
    for line in tqdm(lines, desc="translate"):

        if line == '\n' and tran:
            trans_lines.append(line)
            tran = False
            index = 0
            continue

        if index < 2 and not tran:
            trans_lines.append(line)
            index += 1
            continue

        if index == 2 and not tran:
            tran = True
            index = 3  # for the iteration won't go inside this if anymore

        if tran and index == 3:
            text = translator.translate(line, language).text
            
            file.write(text + '\n')
