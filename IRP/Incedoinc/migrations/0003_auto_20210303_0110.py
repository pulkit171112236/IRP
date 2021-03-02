# Generated by Django 3.1.7 on 2021-03-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incedoinc', '0002_auto_20210302_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='open_to_internal',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='job',
            name='requisition_status',
            field=models.CharField(choices=[('Open', 'Open'), ('Offered', 'Offered'), ('On-hold', 'On-hold'), ('Closed', 'Closed')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='requisitioncandidate',
            name='candidate_status',
            field=models.CharField(choices=[('Selected', 'Selected'), ('Rejected', 'Rejected'), ('On-hold', 'On-hold'), ('Offered', 'Offered'), ('Joined', 'Joined'), ('In-Progress', 'In-Progress')], default='In-Progress', max_length=20),
        ),
    ]