# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('article', '0001_initial')]

    operations = [
        migrations.AlterField(
            field = models.IntegerField(default=0),
            name = 'likes',
            model_name = 'article',
        ),
    ]
