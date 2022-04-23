from googletrans import Translator
from tqdm import tqdm


def srt_tran(file_path: str, language: str):
    translator = Translator()
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open('heb.srt', 'w') as file:
        i = 0
        tran = False
        for line in tqdm(lines, desc="translate"):

            if line == '\n' and tran:
                file.write(line)
                tran = False
                i = 0
                continue

            if i < 2 and not tran:
                file.write(line)
                i += 1
                continue

            if i == 2 and not tran:
                tran = True
                i = 3  # for the iteration won't go inside this if anymore

            if tran and i == 3:
                text = translator.translate(line, language).text
                file.write(text + '\n')


if __name__ == '__main__':
    file_path = input("Enter the path to the subtitles file: ")
    language = input("Enter the language you wish (in English): ")
    srt_tran(file_path, language)

