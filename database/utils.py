import os
from conf.settings import settings


def fetch_database_models():
    models_path = settings.BASE_DIR.joinpath(os.path.join('database', 'models'))
    models_in_dir = [
        i for i in models_path.iterdir() if all([
            i.is_file(),
            i.suffix == '.py',
            not '__' in i.name
        ])
    ]

    return [f'database.models.{model_name.name.removesuffix(model_name.suffix)}' for model_name in models_in_dir]

