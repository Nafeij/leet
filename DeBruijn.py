from typing import Iterable, Any

def de_bruijn(k: Iterable[str] | int, n: int) -> str:
    """
    de Bruijn sequence for alphabet k
    and subsequences of length n.
   
    Such is a circular sequence of symbols such that each
    possible length-n sequence appears exactly once as
    one of its contiguous subsequences.
    
    """
    
    # Two kinds of alphabet input: an integer expands
    # to a list of integers as the alphabet..

    if isinstance(k, int):
        alphabet = list(map(str, range(k)))
    else:
        # While any sort of list becomes used as it is
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []


    """
    If one concatenates together, in lexicographic order,
    all the Lyndon words that have length dividing a given
    number n, the result is a de Bruijn sequence.
    
    """
    def db(t, p):
        print(f"t: {t}, p: {p}\nSeq: {sequence}\na  : {a}\n")
        if t > n:
            if n % p == 0:
                sequence.extend(a[1 : p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

def main():
    print(de_bruijn(2,4))
    # print(de_bruijn("abcd",2)) 

if __name__ == "__main__":
    main()
