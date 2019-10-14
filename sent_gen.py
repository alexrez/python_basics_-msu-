import urllib.request
import random
import sys

Words = open('google-10000-english.txt').read().split()

Len = int(sys.argv[1]) if len(sys.argv)>1 else 20
while Len > len(Words):
    Words *=2

Prep = random.sample((list(",!.:;")+[""]*12)*(Len//10),Len)
Sent = random.sample(random.sample(Words, 2 * Len // 3)*2,Len)

def genit(sent, prep):
    S = Sent[:]
    random.shuffle(S)
    S = " ".join(S)
    P = list(prep)
    random.shuffle(P)
    for i in range(len(Sent)//4):
        j = random.randrange(len(S))
        S = S[:j] + S[j].swapcase() + S[j+1:]
    return " ".join(s+P[i] for i,s in enumerate(S.split()))

print(genit(Sent, Prep))
print(genit(Sent, Prep))