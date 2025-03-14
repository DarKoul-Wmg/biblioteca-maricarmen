from django.core.management.base import BaseCommand
from faker import Faker
from random import randint, choice
from biblioteca.models import Llibre, Usuari, Llengua, Exemplar  # Asegúrate de importar también Exemplar

class Command(BaseCommand):
    help = 'Genera datos ficticios para la base de datos'

    def handle(self, *args, **kwargs):
        fake_es = Faker('es_ES')  # Español
        fake_en = Faker('en_US')  # Inglés
        fake_fr = Faker('fr_FR')  # Francés
        fake_la = Faker('la')  # Latín
        
        llengües = ['Espanyol', 'Català', 'Anglès', 'Francès']
        
        # Crear llibres
        for _ in range(50):
            llengua = choice(llengües)
            if llengua == 'Espanyol':
                fake = fake_es
            elif llengua == 'Català':
                fake = fake_la  # Generar directamente en latín
            elif llengua == 'Anglès':
                fake = fake_en
            else:
                fake = fake_fr
            
            titol = fake.sentence(nb_words=4)
            llengua_obj, _ = Llengua.objects.get_or_create(nom=llengua)  # Obtener o crear la instancia de Llengua
            
            # Crear 2 exemplares para cada llibre

           
            
            # Crear el Llibre (esto va dentro de yun for de 2 para crear dos ejemplares
            llibre = Llibre.objects.create(
                titol=titol,
                autor=fake.name(),
                llengua=llengua_obj,  # Ahora asignamos la instancia de Llengua
                ISBN=fake.isbn13(),
                pagines=randint(100, 1000)
            )
            

            self.stdout.write(self.style.SUCCESS(f'Llibre creat: {llibre.titol} - Llengua: {llibre.llengua.nom}'))

        # Crear usuaris
        for _ in range(50):
            usuari = Usuari.objects.create(
                username=fake_es.user_name(),
                first_name=fake_es.first_name(),
                last_name=fake_es.last_name()
            )
            self.stdout.write(self.style.SUCCESS(f'Usuari creat: {usuari.username}'))
        
        self.stdout.write(self.style.SUCCESS('Dades fictícies generades correctament!'))
