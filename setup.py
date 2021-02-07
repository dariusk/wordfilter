from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wordfilter",
    version="0.2.7",
    license="MIT",
    author="Darius Kazemi",
    description="""A small module meant for use in text generators that lets
    you filter strings for bad words.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dariusk/wordfilter",
    packages=["wordfilter"],
    package_dir={"wordfilter": "lib"},
    package_data={"wordfilter": ["badwords.json"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Communications",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Intended Audience :: Developers"
    ],
    python_requires=">=3"
)
