def main():

    file_name = input("File name: ").split(".")
    print(file_name)
    if len(file_name) >= 2: 
        if file_name[1] == "gif":
            print("image/gif")
        elif file_name[1] == "jpg":
            print("image/jpg")
        elif file_name[1] == "jpeg":
            print("image/jpeg")
        elif file_name[1] == "png":
            print("image/png")
        elif file_name[1] == "pdf":
            print("image/pdf")
        elif file_name[1] == "txt":
            print("image/txt")
        elif file_name[1] == "zip":
            print("image/zip")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")
main()