from github import Github


def main():
    # contains structure for controlling the script
    githubInit()


def getGitToken():
    # get GitToken from a file or user input
    try:
        with open("token", "r") as f:
            return f.read()
    except:
        token = input("Please Enter a token: ")
        if input("Do you want to safe the token for future use? Type y/n: ").lower() == "y":
            f = open("token", "w")
            f.write(token)
        return token


def getGitUsername():
    try:
        with open("username", "r") as f:
            return f.read()
    except:
        username = input("Please Enter a username: ")
        if input("Do you want to safe the username for future use? Type y/n: ").lower() == "y":
            f = open("username", "w")
            f.write(username)
        return username


# def getCreds():

def createConf():
    conf = {}

    if input("Do you want to build a private repo? Type y/n: ").lower() == "y":
        conf["private"] = True

    if input("Do you want to init the repo? y/n: ").lower() == "y":
        conf["init"] = True

    if input("Do you want to use a gitignore template? y/n: ").lower() == "y":
        g.get_gitignore_templates()
        conf["gitignore"] = input(
            "Enter Template name (e.g. Python, Ruby): ")
    else:
        conf["gitignore"] = ""

    # if input("Do you want to safe the current config? Type y/n: ").lower() == "y":
    #     pass

    return conf


def githubInit():

    creds = {}

    creds["token"] = getGitToken()
    creds["username"] = getGitUsername()

    g = Github(creds["token"])

    repo_name = input("Please enter a repo name: ")

    conf = createConf()

    try:
        g.get_user().create_repo(name=repo_name, private=conf["private"], auto_init=conf["init"],
                                 gitignore_template=conf["gitignore"], description=input("Enter a description: "))

    except Exception as e:
        print("Something went wrong, exception: " + str(e))


if __name__ == "__main__":
    main()
