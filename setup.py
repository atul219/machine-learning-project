from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """This function will return list of requirements

    Args:
        file_path (str): _description_

    Returns:
        List[str]: _description_
    """
    HYPHEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
name= "mlproject",
version = '0.0.1', 
author = "Atul",
author_email = "atulyadav219@gmail.com",
packages= find_packages(),
install_requires = get_requirements('requirements.txt')

)


