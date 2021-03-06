# Generated by Django 2.2.5 on 2019-09-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='')),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='employersdetails',
            name='firebase',
            field=models.CharField(default='0', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freelancersdetails',
            name='firebase',
            field=models.CharField(default='0', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employersdetails',
            name='profile_pic',
            field=models.ManyToManyField(to='AdminPanel.Images'),
        ),
        migrations.AddField(
            model_name='freelancersdetails',
            name='profile_pic',
            field=models.ManyToManyField(to='AdminPanel.Images'),
        ),
    ]
