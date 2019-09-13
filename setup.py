from setuptools import setup
import os.path

setup(
    name='mandrill-for-py3',
    version='1.0.58',
    author='Woody',
    author_email='woodythewoodpecker@protonmail.com',
    description='A modified version based on Mandrill Python API client version 1.0.58.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    license='Apache-2.0',
    keywords='mandrill email api',
    url='https://github.com/woodythewoodpecker/mandrill-for-py3.git',
    scripts=['scripts/mandrill', 'scripts/sendmail.mandrill'],
    py_modules=['mandrill'],
    install_requires=['requests >= 0.13.2', 'docopt == 0.4.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Communications :: Email'
    ]
)
