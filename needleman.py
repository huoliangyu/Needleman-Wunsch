#!/usr/bin/python


from __future__ import print_function, division
import numpy as np

match = int(input("match degerini giriniz:"))
mismatch = int(input("mismatch degerini giriniz:"))
gap = int(input("gap degerini giriniz:"))

ptr = {'match': match, 'mismatch': mismatch, 'gap': gap}

f = open("input.txt", "r")
dlis = f.read().split("\n")
ff = open("output.txt", "w")

dna1,dna2 = dlis[0],dlis[1]
m, n = len(dna1), len(dna2)
space = np.zeros((m + 1, n + 1))


def control(x, y):
    if x == y:
        return ptr['match']
    elif x == '-' or y == '-':
        return ptr['gap']
    else:
        return ptr['mismatch']


def skore(m, n):
    for i in range(m + 1):
        space[i][0] = ptr['gap'] * i
    for j in range(n + 1):
        space[0][j] = ptr['gap'] * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = space[i - 1][j - 1] + control(dna1[i - 1], dna2[j - 1])
            up = space[i - 1][j] + ptr['gap']
            left = space[i][j - 1] + ptr['gap']
            space[i][j] = max(diag, up, left)
    for i in space:
        ff.writelines(str(i))
        ff.writelines("\n")

    account(m, n);


def account(m, n):

    i, j = m, n
    way1, way2 = '', ''

    while i > 0 and j > 0:
        location = space[i][j]
        space_diag = space[i - 1][j - 1]
        space_left = space[i][j - 1]
        space_up = space[i - 1][j]

        if location == space_diag + control(dna1[i - 1], dna2[j - 1]):
            a1, a2 = dna1[i - 1], dna2[j - 1]
            i, j = i - 1, j - 1
        elif location == space_up + ptr['gap']:
            a1, a2 = dna1[i - 1], '-'
            i -= 1
        elif location == space_left + ptr['gap']:
            a1, a2 = '-', dna2[j - 1]
            j -= 1
        way1 += a1
        way2 += a2

    while i > 0:
        a1, a2 = dna1[i - 1], '-'
        way1 += a1
        way2 += a2
        i -= 1

    while j > 0:
        a1, a2 = '-', dna2[j - 1]
        way1 += a1
        way2 += a2
        j -= 1

    way1 = way1[::-1]
    way2 = way2[::-1]
    s = ''
    finish= 0
    b = 0
    l = len(way1)
    for i in range(l):
        a1 = way1[i]
        a2 = way2[i]
        if a1 == a2:
            b += 1
            finish += control(a1, a2)

        else:
            finish += control(a1, a2)


    b = b / l * 100
    ff.writelines("\n\n")
    ff.writelines("\n" + "Best Needleman-Wunsch "+"\n")
    ff.writelines(way1+"\n")
    ff.writelines(way2+"\n\n")
    ff.writelines("Score table")
    ff.writelines("\n" + 'Best aligment = %2.1f finish score' % b)
    ff.writelines("\n" + 'Score = %d\n' % finish)


if __name__ == '__main__':
    skore(m, n)







