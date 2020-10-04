from setuptools import setup, find_packages


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


packages = find_packages(exclude=['tests*'])
requirements = requirements()

setup(name='moodlepy',
      version='0.14.2',
      description='Client for moodle webservice',
      author='Habib Rohman',
      author_email='habibrohman@protonmail.com',
      url='https://github.com/hexatester/moodlepy',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Education :: LMS',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      packages=packages,
      install_requires=requirements,
      entry_points={'console_scripts': ['moodle=moodle.__main__:main']})
