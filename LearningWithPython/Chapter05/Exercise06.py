def get_grade(m):
    g = "F3"

    if m >= 75:
        g = "First"
    elif 70 <= m < 75:
        g = "Upper Second"
    elif 60 <= m < 70:
        g = "Second"

    return g

def main():
    xs = [83, 75, 74.9]
    for s in xs:
        print(s, get_grade(s))

main()