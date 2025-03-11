def happy():
    print("  *****  ")
    print(" *     * ")
    print("*  O O  *")
    print("*   ^   *")
    print("* \\___/ *")
    print(" *     * ")
    print("  *****  ")

def sad():
    print("  *****  ")
    print(" *     * ")
    print("*  O O  *")
    print("*   ^   *")
    print("* /___\\ *")
    print(" *     * ")
    print("  *****  ")

def surprised():
    print("  *****  ")
    print(" *     * ")
    print("*  O O  *")
    print("*   ^   *")
    print("*   O   *")
    print(" *     * ")
    print("  *****  ")

output = input("Enter your mood: ")
if output == "happy":
    happy()
elif output == "sad":
    sad()
elif output == "surprised":
    surprised()
else:
    print("Invalid mood")
