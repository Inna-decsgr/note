# Generated by Django 5.1.1 on 2024-10-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0003_memo_is_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
