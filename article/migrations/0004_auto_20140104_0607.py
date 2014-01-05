# encoding: utf8
from django.db import models, migrations
import article.models


class Migration(migrations.Migration):
    
    dependencies = [('article', '0003_article_thumbnail')]

    operations = [
        migrations.AddField(
            field = models.IntegerField(default=0),
            name = 'unlikes',
            model_name = 'article',
        ),
        migrations.AlterField(
            field = models.FileField(upload_to=article.models.get_upload_file_name, blank=True),
            name = 'thumbnail',
            model_name = 'article',
        ),
    ]
