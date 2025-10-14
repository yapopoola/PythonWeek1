import os
import sys


# Gets the current working directory.
# print(os.getcwd())

# Changing director from the current one to the specified one.
# print(os.getcwd())
# os.chdir("../")  # change to the folder before the current folder that we are in.
# print(os.getcwd())

# Create one new directory.
# print(os.mkdir("quizzes"))
# parent_folder = "C:\\Users\\rafi\\Desktop\\PyClasses\\PythonWeek1\\yusuf_assigments"
# print(os.mkdir(f"{parent_folder}\\week_10"))

# Removes only the specified directory from your Operating System.
# print(os.rmdir("yusuf_assigments"))

# Create multiple directories at once
# parent_folder = "C:\\Users\\rafi\\Desktop\\PyClasses\\PythonWeek1\\yusuf_assigments"
# print(os.makedirs(f"{parent_folder}\\week_10"))

# Remove multiple directories from the specified path at once. Starts by deleting the specified dir and then 
# attempts to delete the parent directory of the specified one if the parent directory is empty
# print(os.removedirs("yusuf_assigments"))

# List all the modules in the specified directory
# files_and_folders = os.listdir()
# for module in files_and_folders:
#     try:
#         os.rmdir(module)
#     except OSError:
#         os.remove(module)


# Modifying file permissions using the OS module.
# print(os.chmod("yusuf_assigments", 0o700))    #modify the read permission for the owner of the file

# print(os.fchown)

# 4, 2, 1
# r, w, x


# owner, group, User
# 7        4      5

# Get the name of the OS dependent module
# print(os.name)

# Rename a file using OS
# os.rename("bella.txt", "BELLA.py")

# os.path.exists()


#  --------------------------------------------------------SYS-----------------------------------------------------
params = sys.argv
if not "-v" in params: 
    requested_version = input("No python version detected. Please provide the python version you want: ")
if not "--git.provider" in params: 
    sys.exit("No git provider detected. You are expected to provide the git provider you want using the --git.provider flag")

requested_version = params[2]
users_email = params[4]
users_pasword = params[6]
requested_git_provider = params[8]

print(f"Installing python version {requested_version}")
print(f"Logging in to {requested_git_provider} using the email '{users_email}' and password {'*' * len(users_pasword)}", end="\n\n")
print(f"Successfully logged in user {users_email}")
print(f"Successfully downloaded python version {requested_version}")
