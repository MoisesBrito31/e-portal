# Generated by Django 4.2 on 2023-05-31 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0003_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('color', models.CharField(default='FF0000', max_length=8, verbose_name='cor')),
            ],
        ),
        migrations.AddField(
            model_name='os',
            name='state',
            field=models.CharField(default='0', max_length=500, verbose_name='Estado'),
        ),
    ]
