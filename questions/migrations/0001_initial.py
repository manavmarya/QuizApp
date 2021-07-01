# Generated by Django 3.2.5 on 2021-07-01 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField(max_length=1000)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SubQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempted_Choice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.choice')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
            ],
        ),
    ]
