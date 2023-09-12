from setuptools import setup, find_packages

def read(fname):
    with open(fname, "r") as f:
        return f.read()

# Lee el contenido del archivo README.md
long_description = read('README.md')

setup(
    name="django-times",
    version="0.1.3",
    description="Una biblioteca para trabajar con fechas y horas en Django dentro de los templates.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Estuardo Ramírez",
    author_email="contacto@estuardo.dev",
    url="https://github.com/estuardodev/django-times",
    download_url='https://github.com/estuardodev/django-times.git',
    keywords=['estuardodev', 'django-times', 'django', 'times', 'python times', 'python', 'times django'],
    packages=find_packages(),
    install_requires=["Django>=3.2", 'pytz', 'babel'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Bug Tracking',
    ],
    package_data={
        'django_times': ['static/*.*', 'static/*/*.*'],  
    },
)
