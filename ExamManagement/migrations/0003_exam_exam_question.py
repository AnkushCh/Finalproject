# Generated by Django 3.1.1 on 2020-09-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamManagement', '0002_auto_20200919_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_question',
            field=models.FileField(default='exam/questions/sample.pdf', upload_to='exam/questions'),
        ),
    ]