# This program prompts the user for the name of a file and then outputs that 
# file's media type

file_name = input("File name: ").lower().strip()

if file_name.endswith(".jpg") == True or file_name.endswith(".jpeg") == True:
    print ("image/jpeg")
elif file_name.endswith(".gif") == True:
    print("image/gif")
elif file_name.endswith(".png") == True:
    print("image/png")
elif file_name.endswith(".pdf") == True:
    print("application/pdf")
elif file_name.endswith(".txt") == True:
    print("text/plain")
elif file_name.endswith(".zip") == True:
    print("application/zip")
else:
    print("application/octet-stream")