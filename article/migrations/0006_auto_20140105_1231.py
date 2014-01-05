# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('article', '0005_comment')]

    operations = [
        migrations.RenameField(
            new_name = 'first_name',
            model_name = 'comment',
            old_name = 'author',
        ),
        migrations.AddField(
            field = models.CharField(default='', max_length=20),
            preserve_default = False,
            name = 'second_name',
            model_name = 'comment',
        ),
        migrations.RenameField(
            new_name = 'pub_date',
            model_name = 'comment',
            old_name = 'created',
        ),
    ]
