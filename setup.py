import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="ts_list",
	version="0.0.1",
	author="jaflo",
	description="Ensures lists of strings remain type-safe.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/jaflo/typesafelist",
	packages=setuptools.find_packages(),
	install_requires=["nltk"],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
