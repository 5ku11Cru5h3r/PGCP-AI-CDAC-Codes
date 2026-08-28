def custom_title_case_formatter():
    s = input()
    v = s.split()
    v=[i.capitalize() for i in v]
    x=" ".join(v)
    print(x)


custom_title_case_formatter()