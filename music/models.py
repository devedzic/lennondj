from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField, ForeignKey, DateField, BooleanField
from django.urls import reverse

from datetime import date

"""
Create some model(s) in the <app>/models.py file
    typical fields:
        models.CharField(max_length=<n>, default='<...>')
        models.BooleanField(verbose_name=<verbose name>, 
		    		        choices=<choices_list>, 
		    		        default=<choice from choices_list>,
		    		        ...)
        models.DateField(null=True, blank=True)
        models.TimeField(null=True, blank=True,
		    		     default=datetime.time(hour=<int>, minute=<int>, second=<int>))
        models.ForeignKey(<AnotherModel>,
		                  on_delete=models.SET_NULL,	# CASCADE, SET_DEFAULT,…
		                  null=True, 
		                  blank=True)
        ...
	typical methods:
	    __str__()
        get_absolute_url()		# return reverse('<model>-detail', args=[str(self.id)])
        ...
Register each model in <app>.admin.py with a separate line like:
    admin.site.register(<Model>)
Run:
    manage.py@<project_site>  > makemigrations <app>
Run:
    manage.py@<project_site>  > migrate
in order to create those model tables in your database
Run another cycle of change models - makemigrations - migrate whenever you make changes to your model(s) / database
Run (optionally):
    manage.py@<project_site>  > sqlmigrate <app> <migration number> 
    (e.g., manage.py@polls_site  > sqlmigrate polls 0001) 
to see the SQL equivalent of a specific migration
"""


class Band(models.Model):
    """The model class describing the concept of a band.
    It includes the band's name, country, and the start and end years.
    """

    name = CharField(max_length=50, default='unknown')
    country = CharField(max_length=50, default='unknown')
    start = IntegerField(null=True, blank=True, default=1962, verbose_name='The year the band started playing together')
    end = IntegerField(null=True, blank=True, default=1970, verbose_name='The year the band stopped playing together')

    def __str__(self):
        return f'{self.name} ({self.start if self.start else "..."}-{self.end if self.end else "..."}), {self.country}'

    def get_absolute_url(self):
        """Returns the URL to access a particular Band instance.
        Enables specific Band pages in admin to include the "View on site" button.
        """

        return reverse('band-detail', args=[str(self.id)])


class Musician(models.Model):
    """The model class describing the concept of a musician.
    It includes the musician's name, reference to the musician's band, their birth date, their primary instrument and
    if they are alive or deceased.
    """

    INSTRUMENT = [
        ('lead guitar', 'lead guitar'),
        ('rhythm guitar', 'rhythm guitar'),
        ('bass', 'bass'),
        ('drums', 'drums'),
        ('vocals', 'vocals')
    ]

    ALIVE = [
        (True, 'alive'),
        (False, 'deceased')
    ]

    name = CharField(max_length=50, default='unknown')
    band = ForeignKey(Band, null=True, blank=True, on_delete=models.SET_NULL)
    born = DateField(null=True, blank=True)
    instrument = CharField(max_length=30, choices=INSTRUMENT, verbose_name='Primary instrument', default='unknown')
    alive = BooleanField(verbose_name='Alive/Deceased', choices=ALIVE, default='alive')
    quote = CharField(max_length=200, default='', null=True, blank=True)

    def __str__(self):
        name_str = f'{self.name}, '
        instrument_str = f'{self.instrument} '
        band_str = f'({self.band if self.band else "solo musician"}), '
        born_str = f'born {self.born.isoformat()}; ' if self.born else 'birth date unknown; '
        # if self.born and isinstance(self.born, date):
        #     born_str = self.born.isoformat()
        # else:
        #     born_str = 'birth date unknown'
        alive_str = f'{"alive" if self.alive else "deceased"}'
        return name_str + instrument_str + band_str + born_str + alive_str

    def get_absolute_url(self):
        """Returns the URL to access a particular Musician instance.
        Enables specific Musician pages in admin to include the "View on site" button.
        """

        return reverse('musician-detail', args=[str(self.id)])


