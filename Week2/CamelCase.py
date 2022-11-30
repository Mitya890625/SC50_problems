def main():
    st = input("Type the phrase:\n")
    print(camel_case(st))



def camel_case(str):
    return ''.join(['_'+i.lower() if i.isupper() else i for i in str]).lstrip('_')


main()