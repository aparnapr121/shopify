class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseConfig(metaclass=Singleton):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True


    def create_instance(self, env='dev'):
        config_map = {
            'dev': DevelopmentConfig,
            'qa': StagingConfig,
            'prod': ProductionConfig
        }
        return config_map[env]()


class DevelopmentConfig(BaseConfig):
    pass

class StagingConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass
