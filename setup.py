from setuptools import setup, find_packages

setup(
    name='AdmCO_TP2',
    version='1.0',
    packages=find_packages(exclude=['tests']),
    author="Thomas SANDIER",
    author_email="thomas.sandier@cpe.fr",
    description="Un jeu pierre feuille ciseaux",
)
