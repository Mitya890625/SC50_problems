import re, validators

def main():

    url = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" 
    title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
    clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    '''
    #validator(data)
    #number_checker(data)
    #watch_youtube(url)
    print(validators.email("vargandji@com"))
def validator(data):
    if re.search(r"^Mitya$", data):
        print(f"Hello {data}")
    else:
        print("I dont know you, sir!")
def number_checker(data):
    if re.search(r"^(0?12)($", data):
        print("valid")
    else:
        print("invalid")
def watch_youtube(url):
    matches = re.search(r"https://www\.youtube\.com/embed/xvFZjo5PgG0", url) 
    pulled_str = matches.group()
    new_str = re.sub(r"www\.youtube\.com/embed", "youtu.be", pulled_str)
    print(new_str)
main()

