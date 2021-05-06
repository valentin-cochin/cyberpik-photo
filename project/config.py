from os import path

_base_path = path.dirname(__file__)

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = 'my_precious'

    ML_MODELS_DIR = path.join(_base_path, '..', 'ml_models')
    ASSETS_DEFAULT_DIR = path.join(_base_path, '..', 'resources', 'assets', 'default')
    ASSETS_STYLE_DIR = path.join(_base_path, '..', 'resources', 'assets', 'style')

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass
