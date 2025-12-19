from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    '''
    This returns the requirements 
    '''
    requirements=[]
    with open(filepath) as obj:
        requirements=obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name = 'mlproject',
    version= '0.0.1',
    author='Sudarshan',
    author_email='sudarshangrg36@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)