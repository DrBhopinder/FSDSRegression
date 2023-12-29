from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
    
        requirements = [req for req in requirements if '-e .' not in req]

        #if HYPEN_E_DOT in requirements:
            #requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'Regressor',
    version='0.0.1',
    author='bhopinder',
    author_email='bhopinder92@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)

