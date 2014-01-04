# encoding: utf8
from django.db import models, migrations
import article.models


class Migration(migrations.Migration):
    
    dependencies = [('article', '0002_auto_20131229_1429')]

    operations = [
        migrations.AddField(
            field = models.FileField(default='', upload_to=article.models.get_upload_file_name),
            preserve_default = False,
            name = 'thumbnail',
            model_name = 'article',
        ),
    ]
