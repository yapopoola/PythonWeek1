# ----------------------READING FROM FILES ------------------------
# my_txt_file = open("story_of_my_life.txt", "r")

# my_txt_file.read()  # --> Returns all the content from the specified file

# print(my_txt_file.readline())  # --> Returns one line at a time
# print(my_txt_file.readline())
# print(my_txt_file.readline())

# print(my_txt_file.readlines())  # --> Returns the content as a list where each item in the list is each line in the file.

# my_txt_file.close()

# print(my_txt_file.read())  # --> Would not read from the file after it has been closed.


# ----------------------WRITING TO FILES ------------------------
my_txt_file = open("story_of_us.docx", "w")

# Overwrites the file with all the content you pass into the `.write()` method.
# print(my_txt_file.write("""\nHi! I am the latest content. I don't hate you so much anymore!"""))

# writelines takes a list and writes all the items from that list into your file.
participants = ["Yusuf\n", "Rafihatu\n", "Popoola\n", "Bello\n",]
my_txt_file.writelines(participants)

# for participant in participants:
#     my_txt_file.write(f"Hello {participant}")

# At the end of day, always remember to close your files using `.close()`
my_txt_file.close()