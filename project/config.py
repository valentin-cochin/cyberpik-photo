from os import path


class BaseConfig:
    """Base configuration"""
    # Builtin Configuration
    TESTING = False

    # Directories
    __base_path = path.dirname(__file__)
    ML_MODELS_DIR = path.join(__base_path, '..', 'resources', 'ml_models')
    NST_MODEL_DIR = path.join(ML_MODELS_DIR, 'magenta_arbitrary-image-stylization-v1-256_2')  # From Tensorflow Hub
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
