# Generated by Django 4.2.1 on 2023-11-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_game_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='app.tagpost'),
        ),
    ]