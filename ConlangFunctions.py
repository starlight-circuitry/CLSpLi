import random
import Base


def freqGenerate(phons):
    """
    :param phons: a list of phonemes
    :return: prints a list tuples, (phoneme, frequency)
    """
    l_freqs = []
    for i in phons:
        f = random.randrange(1, 8000)
        l_freqs.append((i, f))
    print(l_freqs)

# freqGenerate(Base.cons_no_freqs)
# freqGenerate(Base.vowls_no_freqs)

#
# def clustGenerate():
#     """
#     :param cons: a list of consonants in tuples, (consonant, frequency)
#     :return: prints a list of consonant clusters
#     """
#     clusts = []
#     stops = ['p', 'k', 't', 'd', 'b', 'ɢ', 'P', 'K', 'T', 'D', 'B', 'Q', 'G']
#     frics = ['ð', 'v', 'f', 'x', 'Z', 'θ', 'ɧ', 'h', 's', 'z', 'ɦ']
#     nasals = ['m', 'ŋ']
#     approx = ['r', 'j', 'w']
#     noclust = ['ⱱ', 'ʔ']
#     for i in stops:
#         for j in frics:
#             clusts.append(i+j)
#     print(clusts)
#
#
# clustGenerate()
