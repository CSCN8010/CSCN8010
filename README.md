<iframe src="https://github.com/TessaAyv79/CSCN8010/blob/main/LAB6.html" width="800" height="600"></iframe>

Welcome ot the CSCN8010 course repository. This is where the course notebooks will be (specifically, they will be in the `class_notebooks` folder. This is what the instructor will present in class)

## Setup
1. You are welcome to `fork` this repository, to get your own copy on your own personal account. `Clone` this fork to your laptop.
2. It is advised to create a new folder which will contain the class notebooks with your own editions. This way, you will have the original notebooks in the `class_notebooks` and your modified notebooks in your own folder. This is helpful specifically since the files are Jupyter notebooks, whose metadata and cell outputs can make `git diff` for syncing changes a bit of a mess sometimes. 
3. Create a virtual environment, run the following commands from the root folder:
    1. Initialize a virtual environment: `python -m venv venv/CSCN8010_classic_ml`
    2. Activate the virtual environment:
        1. Linux or Mac: `source ./venv/CSCN8010_classic_ml/bin/activate`
        2. Windows Powershell: `.\venv\CSCN8010_classic_ml\Scripts\Activate.ps1`
    3. Install the Python packages: `pip install -r requirements.txt`
    4. Install ipykernel: `python -m ipykernel install --user --name=CSCN8010_classic_ml --display-name=CSCN8010_classic_ml`
4. Setting Up vscode to work with Notebooks and Virtual Environments:
    1. vscode needs to be restarted after setting up the virtual environments for the first time. Otherwise, the environments will not be visible in vscode.
    2. To run Python notebooks in vscode, you first need to install the Python extension by Microsoft (done via the Extensions menu on the left sidebar).
    3. Then, open a notebook and set the right kernel (either python_cpu or tensorflow_cpu, depending of what the notebook is using). Setting the kernel is done on the top right side in vscode.
    4. Note that if you see wiggly orange lines below the package names in the import statement, change the interpreter to that of the virtual environment by typing in the command-palette Python: Select Interpreter ([stackoverflow](https://stackoverflow.com/a/72721797/10006823)).
5. Test your environment by running the test file in the `class_notebooks` folder.
