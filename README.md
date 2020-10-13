# PythonAutoGit 

Script I made to make everyones coding easier (fun fact this repo was made and commited by my script)

## What is it for?

It's basically scirpt that allows you commit, make local project folder, open projects and make repos (private also)

### How to build/use?

Just clone source code and put files to easy to access for you folder, then use [this](https://www.youtube.com/watch?v=Y2q_b4ugPWk) tutorial to set up Environment PATH, and fill `config.py` with your things

Remember to insyall requirements using
`pip install -r requirements.py`

Then run `setup.py` using `python setup.py`

Now if you setted up PATH environment correcly you can use `project` command in your powershell/cmd

```
COMMANDS:
project create <name_of_project> <local>(if you dont want to do repo on github) <--true>(if you want repo to be private)
project commit <name_of_project> <commit note>
project open <name_of_project>
```