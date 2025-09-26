
# msvcrt module microsof visual c run time (to read keystrokes without showing the actual characters)
import msvcrt
# import getpass
import sys

# username , password

print(sys.version)
print(sys.platform)

def user_pass(prompt="password"):

    # next line ask to user type your password
    sys.stdout.write(prompt)
    sys.stdout.flush()
    buf = []
    # below line read keystrokes in unicode (It is used to read a single wide character)
    while True:
        ch = msvcrt.getwch()
        if ch in ("\r", "\n"):
            break
        elif ch == "\x08":
            if buf:
                buf.pop()
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        elif ch == "\x03":
            raise KeyboardInterrupt
        else:
            buf.append(ch)
            sys.stdout.write("*")
            sys.stdout.flush() 

    sys.stdout.write("\n") 
    return "".join(buf)


# User Interaction to this code only
username = input("Enter your name: ")
password = user_pass("Enter your password: ")
print("\n")
print("User Details: ")
print("Username:", username, "|", "Password:", password)
