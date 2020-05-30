import zipfile
import os
import io


corpus_content = ""

with zipfile.ZipFile('Sinai-corpus.zip') as z:
    print("Loading {} File(s) ...".format(len(z.namelist())))
    for filename in z.namelist():
        if not os.path.isdir(filename):
            with z.open(filename) as zfile:
                with io.TextIOWrapper(zfile, encoding="utf-8") as file:
                    corpus_content += file.read()
                
                    

words = corpus_content.split()
words_unique = list(set(words))
sentence = corpus_content.split("\n")
sentence_unique = list(set(sentence))


print("({}/{}) Words".format(len(words_unique), len(words)))
print("({}/{}) Sentences".format(len(sentence_unique), len(sentence)))

