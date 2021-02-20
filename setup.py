import setuptools

setuptools.setup(
	name = "scratch-verify",
	version = "1.0.1",
	description = "Verify the ownership of a Scratch account.",
	url = "https://github.com/Richienb/scratch-verify-python",
	keywords = "scratch verify account ownership user",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Typing :: Typed"
	],
	author = "Richie Bendall",
	author_email = "richiebendall@gmail.com",
	license = "MIT",
	python_requires = ">=3.6",
	packages = setuptools.find_packages(),
	long_description = open("readme.md", "r").read(),
	long_description_content_type = "text/markdown",
	install_requires = open("requirements.txt", "r").read().split()
)
