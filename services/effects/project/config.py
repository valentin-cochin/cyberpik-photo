# services/effects/project/config.py

from os import path


class BaseConfig:
    """Base configuration."""

    # Builtin Configuration
    TESTING = False

    # Directories
    __base_path = path.dirname(__file__)
    __resources_dir = path.join(__base_path, '..', 'resources')

    ML_MODELS_DIR = path.join(__resources_dir, 'ml_models')
    NST_MODEL_DIR = path.join(
        ML_MODELS_DIR,
        'magenta_arbitrary-image-stylization-v1-256_2'
    )  # From Tensorflow Hub
    ASSETS_DEFAULT_DIR = path.join(__resources_dir, 'assets', 'default')
    ASSETS_STYLE_DIR = path.join(__resources_dir, 'assets', 'style')

    # Other constants
    ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg']
    EFFECTS = ['nst']
    NST_STYLES = {
        'synthwave-back': 'synthwave-back.jpg',
        'vaporwave-angel': 'vaporwave-angel.png',
        'vaporwave-fluid': 'vaporwave-fluid.jpg',
        'vaporwave-glitch_line': 'vaporwave-glitch_line.jpg'
    }


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    pass


class TestingConfig(BaseConfig):
    """Testing configuration."""

    FLASK_DEBUG = 0
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    pass
