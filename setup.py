from setuptools import setup, find_packages


HYPHEN_E_DOT = "-e ."
def get_requirements(file_path):
    with open(file_path, encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name="mlprpject",
    version="0.1.0",
    author= "Stephen",
    author_email= "shouston11@qub.ac.uk",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),    
)   