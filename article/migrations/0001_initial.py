# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=200),), ('body', models.TextField(),), ('pub_date', models.DateTimeField(verbose_name='date published'),), ('likes', models.IntegerField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Article',
        ),
    ]
