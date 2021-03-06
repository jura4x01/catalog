# Generated by Django 2.1.2 on 2018-10-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personnels', '0003_auto_20181012_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='branch name')),
                ('facade', models.ImageField(blank=True, null=True, upload_to='facades/')),
                ('personnels', models.ManyToManyField(blank=True, help_text='Personnels, registered in this branch.', related_name='branch_set', related_query_name='branch', to='personnels.Personnel', verbose_name='personnels')),
            ],
            options={
                'verbose_name': 'branch',
                'verbose_name_plural': 'branches',
            },
        ),
    ]
