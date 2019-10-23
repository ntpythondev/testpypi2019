import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json2oraparser",
    version="0.0.2",
    author="ntpythondev",
    author_email="nt_python_dev@gmail.com",
    description="Parse json file to oracle database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ntpythondev/testpypi2019.git",
    packages=setuptools.find_packages(),
	include_package_data=True,
	install_requires=[
      'cx_Oracle','pandas' 'PyYAML',
  ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Development Status :: 3 - Alpha",      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		"Intended Audience :: Developers",      # Define that your audience are developers
		#"Topic :: Software Development :: Build Json Parser",

    ],
    
)