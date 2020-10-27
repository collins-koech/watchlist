import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=74ae3b3698d4de9e18b4b5e5afe35f45'
    MOVIE_API_KEY = os.environ.get('74ae3b3698d4de9e18b4b5e5afe35f45')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}