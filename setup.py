import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="wisdom",
    version="0.1.0",
    author="ht-90",
    author_email="",
    description="Wisdom - audio platform to share your wisdom",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ht-90/wisdom",
    packages=setuptools.find_packages(include=["wisdom", "auditory", "registration"]),
    install_requires=[
        "django>=3.1",
        "dj-database-url",
        "Pillow",
        "django-anymail[mailgun]",
        "django-widget-tweaks",
        "psycopg2",
        "django-storages",
        "boto3",
        "python-dotenv",
        "mutagen",
        "Pillow",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 3.1",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
)
