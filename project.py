import sys
import os
import config
from github import Github

path = config.FILEPATH
token = config.TOKENAPI
args = sys.argv

def main(): 
    PRIV_BOOL: bool = False
    try:
        sys.argv[1]
    except:
        print("Error: You didn't provide args!")
        return
    try:
        sys.argv[2]
    except:
        print("Error: Parameters not specified!")
        return
        
    foldername = str(sys.argv[2])
    _dir = path + '\\' + foldername
        
    if sys.argv[1] == "create":
        if "--true" in args:
            args.remove("--true")
            PRIV_BOOL: bool = True
        if "local" in args:
            try:
                args.remove("local")
                args.remove(sys.argv[0])
                args.remove(sys.argv[0])

                _dir = path + '\\' + " ".join(args)

                os.mkdir(_dir)
                os.chdir(_dir)
                os.system('git init')
                os.system(f'echo # {" ".join(args)} > README.md')
                os.system('git add README.md')
                os.system('git commit -m "first commit"')
                
                print(f'{" ".join(args)} created locally.')
                os.system('code .')
                return os.system("TASKKILL /F /IM conhost.exe")
            except Exception as e:
                print(e)
                print(f'{" ".join(args)} was not created!')
                return
        else:
            try:
                args.remove(sys.argv[1])
                args.remove(sys.argv[0])

                g = Github(token)
                user = g.get_user()
                login = user.login
                repo = user.create_repo(" ".join(args), private=PRIV_BOOL)

                _dir = path + '\\' + " ".join(args)
                
                commands = [f'echo # {repo.name} >> README.md',
                            'git init',
                            f'git remote add origin https://github.com/{login}/{repo.name}.git',
                            'git add .',
                            'git commit -m "Initial commit"',
                            'git push -u origin master']
                
                os.mkdir(_dir)
                os.chdir(_dir)
                
                for command in commands:
                    os.system(command)
                    
                print(f'Created repo of name {repo.name}.')
                os.system('code .')
                return os.system("TASKKILL /F /IM conhost.exe")
            except Exception as e:
                print(e)
                print("Creating repo failed!")
                return
    elif sys.argv[1] == "open":
        try:
            args.remove("open")
            args.remove(sys.argv[0])

            _dir = path + '\\' + " ".join(args)

            os.chdir(_dir)
            os.system('code .')
            print(f'Project {" ".join(args)} was opened.')
            return os.system("TASKKILL /F /IM conhost.exe")
        except Exception as e:
            print(e)
            print(f'Project {" ".join(args)} could not be opened!')
            return
    elif sys.argv[1] == "commit":
        args.remove(sys.argv[1])
        try:
            os.chdir(_dir)
            os.system('git add .')
            
            if foldername in args:
                args.remove(foldername)
                args.remove(sys.argv[0])
                
            os.system(f'git commit -m "{" ".join(args)}"')
            os.system('git push origin master')
            
            
            print(f'Commited as {" ".join(args)}.')
        except Exception as e:
            print(e)
            print(f"Commiting failed!")
    else:
        print("Error: Invalid command")
        return
    

if __name__=="__main__":
    main()
