from github import Github


def runner():
    pass


def githubInit():
    creds = {}
    priv_bool = False
    init_bool = False
    gitignore_tpl_name = ""

    creds["username"] = input("Please Enter a username")

    try:
        with open("token", "r") as f:
            creds["token"] = f.read()
    except:
        
        creds["token"] = input("Please Enter a token")


    g = Github(creds["username"],creds["token"])

    repo_name=input("Please enter a repo name")

    

    if input("Do you want to build a private repo? Type y/n").lower() == "y":
        priv_bool = True
    
    if input("Do you want to init the repo? y/n").lower()=="y":
        init_bool = True

    if input("Do you want to use a gitignore template? y/n").lower()=="y":
        g.get_gitignore_templates()
        gitignore_tpl_name = input("Enter Template name (e.g. Python, Ruby)")

    g.get_user().create_repo(name=repo_name, private=priv_bool, auto_init=init_bool, gitignore_template=gitignore_tpl_name, description=input("Enter a description: "))


if __name__ == "__main__":
    githubInit()