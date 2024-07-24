#To install local packages in my local environment (my_proj_env)
from setuptools import find_packages,setup

setup(
    name="mcq_generator",
    version="0.0.1",
    author="shreedhar sanjay jagatap",
    author_email="shreedharjagatap2002@gmail.com",
    install_requires=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)