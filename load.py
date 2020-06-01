import os
import io
import zipfile


def load_corpus():
    corpus_content = ""
    with zipfile.ZipFile('Sinai-corpus.zip') as z:
        print("Loading {} File(s) ...".format(len(z.namelist())))
        for filename in z.namelist():
            if not os.path.isdir(filename):
                with z.open(filename) as zfile:
                    with io.TextIOWrapper(zfile, encoding="utf-8") as file:
                        corpus_content += file.read()

    return corpus_content
