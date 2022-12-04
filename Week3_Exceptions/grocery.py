def grocery():
    groc_dict = {}
    while True:
        try:
            item = input()
        except KeyboardInterrupt:
            print()
            break
        if item in groc_dict:
            groc_dict[item] += 1
        else:
            groc_dict[item] = 1
    for item in sorted(groc_dict.keys()):
        print(groc_dict[item], item.upper())