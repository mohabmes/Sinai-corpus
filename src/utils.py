import re
import os
import numpy as np


def createFile(filename, content, wmode='w'):
    try:
        with open(filename, wmode) as file:
            file.write(content)
    except Exception as e:
        return "Error :", e
    return True


def readFile(filename, rmode='r'):
    try:
        with open(filename, rmode) as file:
            content = file.read()
    except Exception as e:
        return "Error :", e
    return content


def removeNumber(text):
    return re.sub(r'\d+', '', text)


def removeUnnecessaryChar(text):
    text = " ".join(text.split()) # Remove all whitespace in a string
    text = re.sub(r'[،؛﴾﴿٪]+', '', text)
    text = re.sub(r'[\r\t ]+', ' ', text)
    return removeNumber(text)


def removeNonArabicChar(text):
    text = re.sub(
        r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD.0-9]+',
        ' ', text)
    return text


def sentTokenize(text):
    text = re.sub(r'[.؟!,,]', '\n', text)
    return text


def clean(text):
    text = removeUnnecessaryChar(text)
    text = removeNonArabicChar(text)
    return sentTokenize(text)


def scan_directory(dirname):
    files = []
    for filename in os.listdir(dirname):
        files.append(os.path.join(dirname, filename))
    return files


def MED(A, B):
    m = len(A)
    n = len(B)
    D = np.zeros((m + 1, n + 1))
    for i in range(1, m + 1):
        D[i, 0] = i
    for j in range(1, n + 1):
        D[0, j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                alpha = 0
            else:
                alpha = 2

            D[i, j] = min(D[i - 1, j] + 1,
                          D[i, j - 1] + 1, D[i - 1, j - 1] + alpha)
    # print(D[1:])
    return D[m, n]

