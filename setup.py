from setuptools import setup

setup(
    name="consensus-engine",
    version="0.1.0",
    description="Python client for Consensus Engine — query 11 frontier LLMs in parallel.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["consensus_engine"],
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "console_scripts": ["consensus-engine=consensus_engine:main"],
    },
    url="https://github.com/MICONNM/consensus-engine-py",
)
