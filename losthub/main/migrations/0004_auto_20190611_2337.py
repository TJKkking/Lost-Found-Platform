# Generated by Django 2.2.1 on 2019-06-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_itemdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostItemData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('item_time', models.CharField(max_length=20)),
                ('item_location', models.CharField(max_length=50)),
                ('item_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='ItemData',
            new_name='FoundItemData',
        ),
    ]
