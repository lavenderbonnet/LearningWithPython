def hms(ts):
    h = ts // 3600
    rs = ts % 3600
    m = rs // 60
    rs %= 60
    print(h, m, rs)

def test_hms():
    i_s = input()
    s = int(i_s)
    hms(s)

def total(a):
    t = 0
    for n in a:
        t += n
    return t

def product(a):
    p = 1
    for n in a:
        p *= n
    return p

def tp():
    a = [1, 2, 3, 4, 5]
    print(product(a))

def tt():
    a = [1, 2, 3, 4, 5]
    print(total(a))

def print_months():
    for m in ["Jan", "Feb", "Mar"]:
        print(f"One of the months of the year is {m}")

def main():
    # print_months()
    tp()

# if __name__ == "__main__":
main()