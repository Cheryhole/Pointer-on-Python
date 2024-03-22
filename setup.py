import setuptools

with open("README.md","r") as readmefile:
	readme=readmefile.read()

setuptools.setup(
	"Pointer-pkg-tkchen",
	version="0.1",
	author="TkChen",
	author_email="cccyyyhhh135@outlook.com",
	description="A Package that can use the pointers just like in C!",
	long_description=readme,
	long_description_content_type="text/markdown",
	
)