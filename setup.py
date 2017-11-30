from distutils.core import setup

setup(
    name = "seqsero",
    version = "1.0",
    author = "DengLab",
    author_email = "estrain@gmail.com",
    description = ("Serotyping for Salmonella."),
    license = "GPL-2.0",
    keywords = "salmonella",
    url = "https://github.com/estrain/SeqSero",
    packages=['seqsero'],
    scripots['scripts/SeqSero.py'],
    entry_points={
        'console_scripts': ['SeqSero = seqsero.SeqSero:main']
    },
    package_dir = {'seqsero': 'scripts'},
)
