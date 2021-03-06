import sys
import knock30
import knock35
import matplotlib.pyplot as plt
from tqdm import tqdm


def plot(plot_keys, plot_items, png):
    fig = plt.figure()
    plt.scatter(plot_keys, plot_items)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    fig.savefig(png)


def main():
    args = sys.argv
    args.append('ch04/neko.txt.mecab')

    phrase_list = [knock30.parse_mecab(phrase)
                   for phrase in tqdm(knock30.make_phrase_list(args[1]))]
    '''for line in phrase_list:
        for morphological_analysis in line:
            # print(morphological_analysis)
            pass'''
    counter = []
    for number in tqdm(knock35.word_pop_frequency(phrase_list)):
        counter.append(number[1])
    print(counter)
    rank = []
    num = []
    for index, number in tqdm(enumerate(counter)):
        rank.append(index + 1)
        num.append(number)
    print(rank, num)
    plot(rank, num, 'ch04/graph39.png')


if __name__ == '__main__':
    main()
