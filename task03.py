import timeit

# --- Алгоритми пошуку ---
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n, m = len(text), len(pattern)
    lps = build_lps(pattern)

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    d = 256
    h = pow(d, m - 1, prime)
    p = t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for s in range(n - m + 1):
        if p == t and text[s:s + m] == pattern:
            return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % prime
            if t < 0:
                t += prime
    return -1

def boyer_moore(text, pattern):
    bad_char = {char: i for i, char in enumerate(pattern)}
    s = 0
    while s <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

# --- Обмежене читання тексту ---
def read_limited(path, max_len=20000):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()[:max_len]

# --- Алгоритми та шаблони ---
algorithms = {
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp,
    "Boyer-Moore": boyer_moore
}

patterns = {
    "існуючий": "алгоритм пошуку",
    "вигаданий": "неіснуючийпідрядок123"
}

texts = {
    "Стаття 1": read_limited("стаття 1.txt"),
    "Стаття 2": read_limited("стаття 2.txt")
}

# --- Benchmark з обробкою помилок ---
def benchmark(algorithm, text, pattern):
    try:
        print(f"{algorithm.__name__:<12} ...", end=" ")
        t = timeit.timeit(lambda: algorithm(text, pattern), number=1)
        print(f"{t:.6f} сек.")
        return t
    except Exception as e:
        print(f"Помилка: {e}")
        return None

# --- Основний цикл порівняння ---
for text_label, text in texts.items():
    print(f"\n {text_label}\n" + "-"*40)
    for pattern_label, pattern in patterns.items():
        print(f"\n Підрядок: {pattern_label}")
        for name, func in algorithms.items():
            benchmark(func, text, pattern)

