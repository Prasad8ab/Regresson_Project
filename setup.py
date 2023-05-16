from setuptools import find_packages,setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    return requirements    


setup(
    name="RegressionProject",
    version="0.0.1",
    author="PrasadBhagwat",
    author_email="prasad8ab@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)