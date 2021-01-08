import setuptools

setuptools.setup(
	name="scratch-verify-python",
	version="1.0.0",
	description="Verify the ownership of a Scratch account.",
	url="https://github.com/Richienb/scratch-verify-python",
	author="Richie Bendall",
	author_email="richiebendall@gmail.com",
	license="MIT",
	python_requires=">=3.6",
	packages=setuptools.find_packages(),
	long_description=open("readme.md", "r").read(),
	long_description_content_type="text/markdown",
	install_requires=open("requirements.txt", "r").read().split()
)
