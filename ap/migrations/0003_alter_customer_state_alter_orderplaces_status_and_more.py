# Generated by Django 5.1 on 2024-09-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0002_remove_product_city_remove_product_locality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Dhankuta', 'Dhankuta'), ('Rolpa', 'Rolpa'), ('Puythan', 'Puythan'), ('Lamjung', 'Lamjung'), ('Bhaktpur', 'Bhaktpur'), ('Nepaljung', 'Nepaljung'), ('Tulsipur', 'Tulsipur'), ('Pokhara', 'Pokhara'), ('salyan', 'salyan'), ('lalitpur', 'lalitpur'), ('kathamandu', 'kathamandu'), ('DANG', 'DANG'), ('Bardia', 'Bardia'), ('Rukum', 'Rukum'), ('Dharan', 'Dharan')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderplaces',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Cancel', 'Cancel'), ('On The Way', 'On The Way'), ('Pending', 'Pending'), ('Acceppted', 'Accepted'), ('Deivered', 'Deivered')], default='Pending', max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='Brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('T', 'Top wear'), ('B', 'Bottom wear')], default='M', max_length=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_image',
            field=models.ImageField(default='default_image.jpg', upload_to='Product_image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Title',
            field=models.CharField(max_length=50),
        ),
    ]
