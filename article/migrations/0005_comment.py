# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('article', '0004_auto_20140104_0607')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('created', models.DateTimeField(),), ('author', models.CharField(max_length=20),), ('body', models.TextField(),), ('article', models.ForeignKey(to=u'article.Article', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'Comment',
        ),
    ]
