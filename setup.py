from setuptools import setup

setup(
    name="provinces-plugin",
    version="0.1.0",
    packages=["provinces"],
    package_dir={"provinces": "provinces"},
    description="Provinces integration",
    install_requires=["django-cities-light", "django-celery-results"],
    entry_points={
        "saleor.plugins": ["provinces = provinces.plugin:ProvincesPlugin"],
    },
)
