from github import Github


def main():
    # contains structure for controlling the script
    githubInit()


def getGitToken():
    # get GitToken from a file or user input


def getGitUsername():


def getCreds():


def githubInit():

    creds = {}
    priv_bool = False
    init_bool = False
    gitignore_tpl_name = ""

    #######################

    try:
        with open("token", "r") as f:
            creds["token"] = f.read()
    except:
        creds["token"] = input("Please Enter a token: ")
        if input("Do you want to safe the token for future use? Type y/n: ").lower() == "y":
            f = open("token", "w")
            f.write(creds["token"])

    #######################

    try:
        with open("username", "r") as f:
            creds["username"] = f.read()
    except:
        creds["username"] = input("Please Enter a username: ")
        if input("Do you want to safe the username for future use? Type y/n: ").lower() == "y":
            f = open("username", "w")
            f.write(creds["username"])

    #######################

    g = Github(creds["token"])

    repo_name = input("Please enter a repo name: ")

    if input("Do you want to build a private repo? Type y/n: ").lower() == "y":
        priv_bool = True

    if input("Do you want to init the repo? y/n: ").lower() == "y":
        init_bool = True

    if input("Do you want to use a gitignore template? y/n: ").lower() == "y":
        g.get_gitignore_templates()
        gitignore_tpl_name = input(
            "Enter Template name (e.g. Python, Ruby): ")

    if input("Do you want to safe the current config? Type y/n: ").lower() == "y":
        pass

    try:
        g.get_user().create_repo(name=repo_name, private=priv_bool, auto_init=init_bool,
                                 gitignore_template=gitignore_tpl_name, description=input("Enter a description: "))

    except Exception as e:
        print("Something went wrong, exception: " + str(e))


if __name__ == "__main__":
    main()
