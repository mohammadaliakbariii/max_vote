# Generated by Django 3.2.6 on 2021-09-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]