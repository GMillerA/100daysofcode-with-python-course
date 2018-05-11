import Comic_research


def main():
    print("Marvel Comic Book Characters")
    print()
    Comic_research.init()

    print("Count of Good, Bad, and Neutral Characters:")
    #TODO: Count of alignments

    #Comic_research.get_align()
    #for idx, d in enumerate(days[:5]):
    #    print("{}. {} F on {}".format(idx+1, d.actual_max_temp, d.date))
    print()
    print("The characters with the most appearances:")
    heros = Comic_research.most_appearances()
    for d in heros[:5]:
        print("{} has appeared in {} comics".format(d.name, d.APPEARANCES))
    print()
    print("The characters with the earliest appearances:")

    heros = Comic_research.first_appearances()
    for d in heros[:5]:
        print("{} first appeared in {}".format(d.name, d.Year))


if __name__ == '__main__':
    main()