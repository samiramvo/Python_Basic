import sys
def print_to_stderr(*a):
    print(*a,file=sys.stderr)
print_to_stderr("La vie est belle")