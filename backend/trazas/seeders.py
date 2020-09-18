from django_seed import Seed

seeder = Seed.seeder()

from estaciones.models import EstacionModel
from apibackend.models import VolcanModel
seeder.add_entity(VolcanModel, 5)
seeder.add_entity(EstacionModel, 5)


inserted_pks = seeder.execute()