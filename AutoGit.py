from github import Github
import json


def main():
    """contains structure for controlling the script"""
    githubInit()


def getGitToken():
    """ get GitToken from a file or user input """
    try:
        with open("token", "r") as f:
            return f.read()
    except:
        token = input("Please Enter a token: ")
        if input("Do you want to safe the token for future use? Type y/n: ").lower() == "y":
            f = open("token", "w")
            f.write(token)
        return token


def getGithubInstance():
    """ small utility to get the github instance """
    return Github(getGitToken())


def getGitUsername():
    """ unused method for getting the git username"""
    try:
        with open("username", "r") as f:
            return f.read()
    except:
        username = input("Please Enter a username: ")
        if input("Do you want to safe the username for future use? Type y/n: ").lower() == "y":
            f = open("username", "w")
            f.write(username)
        return username


def createConf():
    """creates and returns config for github"""
    conf = {"private": False, "init": False, "gitignore": ""}

    try:
        with open("conf", "r") as f:
            conf = json.load(f)
            print("Config found: ")
            print(conf)
            if input("Use the existing config? Type y/n: ").lower() == "y":
                return conf

    except Exception as e:
        print(
            "Config could not be loaded. Problem with file, or file doesn't exist! " + str(e))

    if input("Do you want to build a private repo? Type y/n: ").lower() == "y":
        conf["private"] = True

    if input("Do you want to init the repo? y/n: ").lower() == "y":
        conf["init"] = True

    if input("Do you want to use a gitignore template? y/n: ").lower() == "y":
        getGithubInstance().get_gitignore_templates()
        conf["gitignore"] = input(
            "Enter Template name (e.g. Python, Ruby): ")

    if input("Do you want to safe the current config? Type y/n: ").lower() == "y":
        json.dump(conf, open("conf", "w"))
        print("config saved")

    return conf


def githubInit():
    """ create new repository """

    repo_name = input("Please enter a repo name: ")

    conf = createConf()

    try:
        g = getGithubInstance().get_user().create_repo(name=repo_name, private=conf["private"], auto_init=conf["init"],
                                                       gitignore_template=conf["gitignore"], description=input("Enter a description: "))

        print("Success! \n%s" % g.clone_url)
    except Exception as e:
        print("Something went wrong, exception: " + str(e))


if __name__ == "__main__":
    main()
