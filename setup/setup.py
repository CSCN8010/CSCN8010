import subprocess
import os
import platform
import sys


def identify_operating_system():
    """
    Identify the core operating system and print it.

    :return: str - The name of the operating system (e.g., 'Windows', 'Linux', 'Darwin')
    """
    return platform.system()


def identify_processor_platform():
    """
    Identify the processor platform.

    :return: str - The processor platform (e.g., 'x86_64', 'AMD64', 'arm64' etc.)
    """
    return platform.machine()


def identify_shell(platform: str):
    """
    Identify the shell environment based on the operating system.

    :param platform: str - The name of the operating system (e.g., 'Windows', 'Linux', 'Darwin')
    :return: str - The shell environment (e.g., 'bash', 'zsh', 'cmd', 'powershell')
    """
    if (platform == 'Linux') or (platform == 'Darwin'):
        shell = os.environ["SHELL"]
    elif platform == 'Windows':
        shell = os.environ["COMSPEC"]
    print(f'Shell: {shell}')
    return shell


def identify_python_executable():
    """
    Identify the filename of the Python interpreter running this script.

    :return: str - The Python executable filename (e.g., 'python', 'python3', 'python.exe', 'python3.exe')
    """
    executable = sys.executable
    print(f'The python executable file is: {executable}')
    if (executable.endswith('python')) | (executable.endswith('python.exe')):
        executable = 'python'
    elif (executable.endswith('python3')) | (executable.endswith('python3.exe')):
        executable = 'python3'
    else:
        raise ValueError(f"executable is {executable} and it doesn't end with neither 'python', 'python.exe', 'python3', nor 'python3.exe'. "
                         "To support this executable, update this script"
                         )
    return executable


def validate_python_version():
    """
    Check if the installed Python version is within the recommended range (3.7.x-3.11.x).
    If not, exit the script with a message.
    """
    if (sys.version_info >= (3, 7)) and (sys.version_info < (3, 12)):
        print(
            f'Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} is installed. '
            '(the recommended version for this repository is 3.7.x-3.11.x)'
        )
    else:
        sys.exit(
            f'The Python version installed is: {sys.version_info.major}.{sys.version_info.minor}, and is not supported. '
            'Please install the recommended version of Python and try again. '
            'See: https://www.python.org/downloads/'
        )


def is_git_installed():
    """
    Check if Git is installed. If not, raise a ValueError with instructions to install it.
    """
    try:
        output = subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE)
        output = output.stdout.decode('ascii').replace('\n', '')
        print(f'Git is installed (version: {output})')
    except subprocess.CalledProcessError:
        raise ValueError(
            'Git is not installed. Please install Git and rerun this script.'
            'To install, see: https://git-scm.com/downloads'
        )


def is_pip_installed():
    """
    Check if pip is installed. If not, raise an ImportError with instructions to install it.
    """
    try:
        import pip
        print(f'pip is installed (version: {pip.__version__})')
    except ImportError:
        raise ImportError('pip is not installed. Please install pip and run this script again')


def is_ensurepip_installed():
    """
    Check if ensurepip is installed. If not, raise an ImportError with instructions to install it.
    """
    try:
        import ensurepip
        print(f'ensurepip is installed (version: {ensurepip.version()})')
    except ImportError:
        raise ImportError('ensurepip is not installed. Please install ensurepip and run this script again')


def create_venv(venv_path: str, platform: str, shell: str, executable: str):
    # create a virtual environment
    if os.path.exists(venv_path):
        print(
            f'{venv_path} - Virtual environment folder already exists. '
            'Skipping venv creation. '
            'If you want to recreate the venv, delete the folder and run this script again.'
        )
        return
    print(f'{venv_path} - Creating virtual environment...')
    subprocess.run(f'{executable} -m venv {venv_path}', shell=True)
    print(f'{venv_path} - Virtual environment created')


def install_packages(venv_path: str, requirements_path: str, platform: str, shell: str, executable: str):
    """
    Install packages from a requirements.txt file into a virtual environment.

    :param venv_path: str - The path to the virtual environment
    :param requirements_path: str - The path to the requirements.txt file
    :param platform: str - The name of the operating system (e.g., 'Windows', 'Linux', 'Darwin')
    :param shell: str - The shell environment (e.g., 'bash', 'zsh', 'cmd', 'powershell')
    :param executable: str - The Python executable filename (e.g., 'python', 'python3', 'python.exe', 'python3.exe')
    """
    print(f'{venv_path} - Installing packages...')
    if (platform == 'Linux') | (platform == 'Darwin'):
        subprocess.run(f'{venv_path}/bin/pip install -r {requirements_path}', shell=True)
    elif platform == 'Windows':
        subprocess.run(fr'{venv_path}\Scripts\pip install -r {requirements_path}', shell=True)
    print(f'{venv_path} - Packages installed')


def install_ipykernel(venv_path: str, venv_name: str, platform: str, shell: str, executable: str):
    """
    Install ipykernel in the specified virtual environment and create a kernel with the specified name and display name.

    :param venv_path: str - The path to the virtual environment
    :param venv_name: str - The name of the virtual environment
    :param platform: str - The name of the operating system (e.g., 'Windows', 'Linux', 'Darwin')
    :param shell: str - The shell environment (e.g., 'bash', 'zsh', 'cmd', 'powershell')
    :param executable: str - The Python executable filename (e.g., 'python', 'python3', 'python.exe', 'python3.exe')
    """
    print(f'{venv_path} - Installing ipykernel...')
    if (platform == 'Linux') | (platform == 'Darwin'):
        subprocess.run(f'{venv_path}/bin/python -m ipykernel install --user --name={venv_name} --display-name={venv_name}', shell=True)
    elif platform == 'Windows':
        subprocess.run(fr'{venv_path}\Scripts\python -m ipykernel install --user --name={venv_name} --display-name={venv_name}', shell=True)
    print(f'{venv_path} - ipykernel installed')


def install_miniconda(miniconda_url: str, miniconda_file_name: str, miniconda_install_path: str = ""):
    """
    Download and install MiniConda at the specified path.

    :param miniconda_url: str - The URL to download the MiniConda installer
    :param miniconda_file_name: str - The name of the downloaded MiniConda installer file
    :param miniconda_install_path: str - The path to install MiniConda (default is '~/miniconda')
    """
    print('Installing MiniConda...')
    if not miniconda_install_path:
        miniconda_install_path = os.path.join(os.path.expanduser('~'), 'miniconda')
    if os.path.exists(miniconda_install_path):
        print('MiniConda is already installed.')
        return
    subprocess.run(f'curl -o {miniconda_file_name} {miniconda_url}', shell=True, check=True)
    subprocess.run(f'bash {miniconda_file_name} -b -p {miniconda_install_path}', shell=True, check=True)
    subprocess.run(f'rm {miniconda_file_name}', shell=True, check=True)
    print('MiniConda installed successfully')


def create_venv_miniconda(venv_name: str, python_version: str, miniconda_install_path: str = ""):
    """
    Create a new Miniconda environment with the specified name and Python version.

    :param venv_name: str - The name of the new Miniconda environment
    :param python_version: str - The Python version to be installed in the new environment (e.g., '3.8')
    :param miniconda_install_path: str - Path where miniconda is installed. (default is '~/miniconda')
    """
    if not miniconda_install_path:
        miniconda_install_path = os.path.join(os.path.expanduser('~'), 'miniconda')
    miniconda_base_path = os.path.join(miniconda_install_path, "bin", "activate")
    print(f'Creating Miniconda environment "{venv_name}" with Python {python_version}...')
    subprocess.run(f'source {miniconda_base_path} && conda create -n {venv_name} python={python_version} --yes',
                   shell=True, check=True)
    print(f'Miniconda environment "{venv_name}" created')


def install_tensorflow_deps_miniconda(venv_name: str, miniconda_install_path: str = ""):
    """
    Only meant for Apple Silicon (M1/M2) Macs.
    Install required packages for Tensorflow in the specified Miniconda environment.

    :param venv_name: str - The name of the Miniconda environment
    :param miniconda_install_path: str - Path where miniconda is installed. (default is '~/miniconda')
    """
    if not miniconda_install_path:
        miniconda_install_path = os.path.join(os.path.expanduser('~'), 'miniconda')
    miniconda_base_path = os.path.join(miniconda_install_path, "bin", "activate")
    print(f'Installing required packages for Tensorflow in "{venv_name}" environment...')
    subprocess.run(
        f'source {miniconda_base_path} && conda activate {venv_name} && conda install -c apple tensorflow-deps --yes', shell=True, check=True)
    print(f'tensorflow-deps installed in "{venv_name}" environment')


def install_requirements_miniconda(venv_name: str, requirements_file: str, miniconda_install_path: str = ""):
    """
    Install required packages from a requirements.txt file in the specified Miniconda environment.

    :param venv_name: str - The name of the Miniconda environment
    :param requirements_file: str - The path to the requirements.txt file
    :param miniconda_install_path: str - Path where miniconda is installed. (default is '~/miniconda')
    """
    if not miniconda_install_path:
        miniconda_install_path = os.path.join(os.path.expanduser('~'), 'miniconda')
    miniconda_base_path = os.path.join(miniconda_install_path, "bin", "activate")
    print(f'Installing required packages in {requirements_file} in "{venv_name}" environment...')
    subprocess.run(
        f'source {miniconda_base_path} && conda activate {venv_name} && python -m pip install -r {requirements_file}', shell=True, check=True)
    print(f'{requirements_file} installed in "{venv_name}" environment')


def configure_shell_config_file(shell: str, miniconda_install_path: str = ""):
    """
    Set the miniconda base environment to auto activate on new shell initialization.

    :param shell: str - The name of shell
    :param miniconda_install_path: str - Path where miniconda is installed. (default is '~/miniconda')
    """
    if 'zsh' in shell:
        shell_config_file = os.path.expanduser('~/.zshrc')
    elif 'bash' in shell:
        if os.path.exists(os.path.expanduser('~/.bash_profile')):
            shell_config_file = os.path.expanduser('~/.bash_profile')
        else:
            shell_config_file = os.path.expanduser('~/.bashrc')
    else:
        raise Exception(f"Could not determine shell_config_file for shell {shell}")

    if not miniconda_install_path:
        miniconda_install_path = os.path.join(os.path.expanduser('~'), 'miniconda')
    miniconda_base_path = os.path.join(miniconda_install_path, "bin", "activate")

    lines_to_add = [
        '# Miniconda base environment',
        f'export PATH="{miniconda_base_path}:$PATH"',
        f'source {miniconda_base_path}'
    ]

    if os.path.isfile(shell_config_file):
        with open(shell_config_file, 'r') as f:
            existing_lines = f.readlines()
    else:
        existing_lines = []

    if not set(lines_to_add).issubset([x.replace("\n", "") for x in existing_lines]):
        with open(shell_config_file, 'a') as f:
            f.write('\n'.join(lines_to_add))
            print(f'Updated {shell_config_file}')
    else:
        print(f'{shell_config_file} already contains the Miniconda configuration')


def identify_rosetta(operating_system: str, processor_platform: str):
    """
    Identify if Rosetta is installed and running on Apple Silicon (M1/M2) Macs.

    :param operating_system: str - The name of the operating system
    :param processor_platform: str - The name of the processor architecture
    """
    if operating_system == 'Darwin':
        if processor_platform == 'x86_64':
            try:
                proc_translated = int(os.popen("sysctl -in sysctl.proc_translated").read().strip())
                return proc_translated == 1
            except (ValueError, OSError):
                pass
    return False


def main():
    operating_system = identify_operating_system()
    processor_platform = identify_processor_platform()
    shell = identify_shell(operating_system)
    is_rosetta = identify_rosetta(operating_system, processor_platform)

    print(f"\nOperating System (OS) detected: {operating_system}")
    print(f"CPU Architecture detected: {processor_platform}")
    print(f"Shell detected: {shell}")
    print(f"Rosetta detected: {is_rosetta}\n")

    # Installation for Windows, Linux, and MacOS running on x86_64 architecture
    if operating_system in ['Windows', 'Linux', 'Darwin'] and processor_platform in ['AMD64', 'x86_64'] and not is_rosetta:
        validate_python_version()
        executable = identify_python_executable()
        is_git_installed()
        is_pip_installed()
        is_ensurepip_installed()
        venv_names = ['pytorch_cpu', 'tensorflow_cpu']
        venv_paths = [os.path.join('.', 'venv', n) for n in venv_names]
        requirements_paths = [os.path.join('.', 'setup', 'requirements_' + e + '.txt') for e in venv_names]
        for venv_path, requirements_path, venv_name in zip(venv_paths, requirements_paths, venv_names):
            create_venv(venv_path, operating_system, shell, executable)
            install_packages(venv_path, requirements_path, operating_system, shell, executable)
            install_ipykernel(venv_path, venv_name, operating_system, shell, executable)

    # Installation for macOS running on Apple Silicon
    elif operating_system == 'Darwin' and (processor_platform in ['arm64', 'arm64e'] or is_rosetta):
        miniconda_url = 'https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh'
        miniconda_file_name = 'Miniconda3-latest-MacOSX-arm64.sh'
        install_miniconda(miniconda_url, miniconda_file_name)

        venv_name = 'tensorflow_metal'
        python_version = '3.10.10'
        create_venv_miniconda(venv_name, python_version)
        install_tensorflow_deps_miniconda(venv_name)
        install_requirements_miniconda(venv_name, "setup/requirements_tensorflow_apple_silicon.txt")
        print(f"\n (1/2) Installation Succesful! Please run \'conda activate {venv_name}\' to activate the environment.")

        venv_name = 'pytorch_metal'
        python_version = '3.10.10'
        create_venv_miniconda(venv_name, python_version)
        install_requirements_miniconda(venv_name, "setup/requirements_pytorch_cpu.txt")
        print(f"\n (2/2) Installation Succesful! Please run \'conda activate {venv_name}\' to activate the environment.")

        configure_shell_config_file(shell)
        print(f"\Please restart your shell window for changes to take affect.")

    else:
        raise Exception(
            f"Could not find a compatible operating system (OS) and CPU Architecture: the platform seems to have OS={operating_system} and CPU architecture={processor_platform}. \
                This setup supports only Windows, Linux or Darwin (Mac) as an OS and x86_64 or arm64 for the CPU architecture.")


if __name__ == '__main__':
    main()
