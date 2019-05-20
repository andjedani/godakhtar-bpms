from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_remove_keyperson_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='key_persons',
        ),
    ]
