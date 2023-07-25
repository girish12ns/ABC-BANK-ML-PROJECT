from setuptools import find_packages,setup

constant="-e ."
def get_tools(file_path:str)->list[str]:

    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()

        requirements=[req.replace("/n","") for req in requirements]

        for pack in requirements:
            if pack==constant:
                requirements.remove(pack)
                
    return requirements



setup(
    name="ABC churn",
    version="0.0.1",
    author="Girish",
    author_email="girish12n@gmail.com",
    packages=find_packages(),
    install_packages=get_tools('requirements.txt')
)