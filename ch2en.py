# Convert Chinese word to random English strings

import argparse
from main import file_split, build_vocab

parser = argparse.ArgumentParser()
parser.add_argument("--train", type=str, default="", help="input file")
parser.add_argument("--output", type=str, default="", help="output file")
parser.add_argument("--min_count", type=int, default=5, help="minimum frequency of a word")

def main(args):
    word2idx, word_list, freq = build_vocab(args)

    ch2en = {}
    for k, v in word2idx.items():
        remain = v % 52
        quotient = v // 52
        if remain < 26:
            s = chr(remain + ord('a'))
        else:
            s = chr(remain - 26 + ord('A'))

        while quotient > 0:
            remain = quotient % 52
            quotient = quotient // 52
            if remain < 26:
                s += chr(remain + ord('a'))
            else:
                s += chr(remain - 26 + ord('A'))
        ch2en[k] = s

    with open(args.train, 'r') as fread, open(args.output, 'w') as fwrite:
        for line in fread:
            words = []
            for w in line.strip().split():
                if w in ch2en:
                    words.append(ch2en[w])
            fwrite.write(' '.join(words) + '\n')


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
