import argparse

# Corpus Documents
documents = {}


# Clean up and Process string lines
def process_str(c):
    result = " ".join(c.split())
    result = result.lower()
    result = result.replace(" ", "_")
    return "___" + result + "___"


# Generate N-grams for each document
def gen_ngram(c, n):
    ptr = 0
    lst = []
    length = len(c)

    while ptr < length:
        if ptr == (length - (n - 1)):
            break
        lst.append(c[ptr:ptr + n])
        ptr += 1

    return lst


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="get corpus data", type=str)
    parser.add_argument("ngram", help="get ngram value", type=int)
    args = parser.parse_args()

    # Read file to get corpus document
    with open(args.filename) as file:
        docs = []
        line = []

        fLines = [line.rstrip() for line in file]
        for i, s in enumerate(fLines):
            if '---' not in s:
                line.append(s)
            else:
                docs.append(''.join(line))
                line = []

            if i == len(fLines) - 1:
                docs.append(''.join(line))

        # Generate NGram for Each document
        for i, data in enumerate(docs):
            line = process_str(data)
            ngram = gen_ngram(line, args.ngram)
            documents[i] = ngram

        print(documents)
