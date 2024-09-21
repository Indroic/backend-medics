import pathlib

from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry 
from .models import Categoria
from core.settings import BASE_DIR

@SeederRegistry.register
class CategoriasSeeder(seeders.CSVFileModelSeeder):
    model = Categoria
    csv_file_path = str(pathlib.Path(BASE_DIR / 'examenes' / 'data' / 'categorias.csv'))