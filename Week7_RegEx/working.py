import re, sys

def main():
    print(convert(input("Hours: ")))
   


def convert(s):
    if ':' in s:
        matches_1 = re.search(r"((\d)?\d:(\d\d)?) am", s)
        hours_am, minutes_am = matches_1.group(1).split(":")
        matches_2 = re.search(r"((\d)?\d:(\d\d)?) pm", s)
        hours_pm, minutes_pm = matches_2.group(1).split(":")
        hours_pm = int(hours_pm) + 12
        new_str_1 = re.sub(r"((\d)?\d:\d\d) am", f"{hours_am}:{minutes_am}", s)
        new_str_2 = re.sub(r"((\d)?\d:\d\d) pm($)?", f"{hours_pm}:{minutes_pm}", new_str_1)
        return new_str_2
    else:
        matches_3 = re.search(r"(\d)? am", s)
        matches_4 = re.search(r"(\d)? pm", s)
        hours_pm_clean = matches_3.group(1)
        hours_pm_clean = int(hours_pm_clean) + 12
        hours_am_clean = matches_4.group(1)
        new_str_3 = re.sub(r"\d am", f"{hours_am_clean}:00", s)
        new_str_4 = re.sub(r"\d pm($)?", f"{hours_pm_clean}:00", new_str_3)
        return new_str_4


if __name__ == "__main__":
    main()