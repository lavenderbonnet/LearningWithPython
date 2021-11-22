# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/17/2021
# --------------------------------------------------------------------------

def split_name(n):
    fn, ln = n.split()
    return (fn, ln)

def main():
    fn, ln = split_name("Lilac Walia")
    print(f"{ln}, {fn}")

main()