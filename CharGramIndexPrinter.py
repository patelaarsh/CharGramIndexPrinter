import argparse


# Clean up and Process string lines
def process_str(c, n):
    result = " ".join(c.split())
    result = result.lower()
    result = result.replace(" ", "_")

    padding = ''.join(["_" for _ in range(n - 1)])

    return padding + result + padding


# Generate N-grams for each document
def gen_ngram(c, n):
    ptr = 0
    lst = []
    length = len(c)

    # Divide and insert same amount of words
    while ptr < length:
        if ptr == (length - (n - 1)):
            break
        lst.append(c[ptr:ptr + n])
        ptr += 1

    return lst


# Generate N-grams database
def gen_database(d, n):
    # Corpus Database
    database = {}

    for idx, data in enumerate(d):
        line = process_str(data, n)
        ngram = gen_ngram(line, n)

        for pos, d in enumerate(ngram):
            if d in database:
                # Update exiting entry
                database[d][2].add((idx, pos))
            else:
                # First entry
                database[d] = [1, 1, {(idx, pos)}]

        # Update entries
        for e in database.values():

            # Count numbers of entries in each
            doc_count = set()
            for c in e[2]:
                doc_count.add(c[0])

            # Update entries counts
            e[0] = len(doc_count)
            e[1] = len(e[2])

    return database


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="get corpus data", type=str)
    parser.add_argument("ngram", help="get ngram count", type=int)
    args = parser.parse_args()

    # Read file to get corpus data
    with open(args.filename) as file:
        # Read all the text of file
        text = file.read()

        # Strip lines to remove new lines
        fLines = [line.strip() for line in text.split("---")]

        # Generate N-Grams database
        corpus_database = gen_database(fLines, args.ngram)
        # print(corpus_database)

        # Printing reverse lookup output in sorted order
        for corp in sorted(corpus_database.keys(), key=lambda k: k.replace('_', '')):
            entry = corpus_database[corp]
            print("{}\n{},{},{}".format(corp, entry[0], entry[1], ''.join([str(x) for x in entry[2]])))
