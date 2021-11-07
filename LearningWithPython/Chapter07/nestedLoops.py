# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/6/2021
# --------------------------------------------------------------------------

students_classes = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])
]

def who_takes_what():
    for (name, subjects) in students_classes:
        print(name, "takes", len(subjects), "courses.")

def num_students_class(n):
    counter = 0
    for (name, subjects) in students_classes:
        for s in subjects:
            if s == n:
                counter += 1
    print(f"The number of students taking {n} is", counter)

def main():
    num_students_class(input())

main()