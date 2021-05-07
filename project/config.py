from os import path


class BaseConfig:
    """Base configuration"""
    # Builtin Configuration
    TESTING = False

    # Directories
    __base_path = path.dirname(__file__)
    ML_MODELS_DIR = path.join(__base_path, '..', 'ml_models')
    ASSETS_DEFAULT_DIR = path.join(__base_path, '..', 'resources', 'assets', 'default')
    ASSETS_STYLE_DIR = path.join(__base_path, '..', 'resources', 'assets', 'style')

    ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg']


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass
