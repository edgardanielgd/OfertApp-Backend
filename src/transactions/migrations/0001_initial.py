# Generated by Django 3.2.16 on 2023-04-20 20:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_auth', '0001_initial'),
        ('publications', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(db_column='usrId', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='account', serialize=False, to='users_auth.user')),
                ('balance', models.DecimalField(db_column='accBalance', decimal_places=0, max_digits=13)),
                ('frozen', models.DecimalField(db_column='accFrozen', decimal_places=0, max_digits=13)),
            ],
            options={
                'db_table': 'ACCOUNT',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(db_column='payId', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('CC', 'Credit Card'), ('PP', 'Pay Pal'), ('NQ', 'Nequi'), ('DV', 'Daviplata'), ('VC', 'Virtual Currency')], db_column='payType', max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_column='payTimestamp')),
                ('amount', models.DecimalField(db_column='payAmount', decimal_places=0, max_digits=13)),
                ('receipt', models.FileField(db_column='payReceipt', upload_to='receipts/')),
                ('flow', models.CharField(choices=[('I', 'Inflow'), ('O', 'Outflow')], db_column='payFlow', max_length=1)),
            ],
            options={
                'db_table': 'PAYMENT',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(db_column='tranId', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('BP', 'Bid Placed'), ('CS', 'Cost Per Sale'), ('BC', 'Bid Revoked'), ('AR', 'Account Recharge'), ('AW', 'Account Withdrawal'), ('AA', 'Admin Adjustment'), ('OT', 'Other')], db_column='tranType', max_length=2)),
                ('description', models.CharField(db_column='tranDescription', max_length=45, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_column='tranTimestamp')),
                ('amount', models.DecimalField(db_column='tranAmount', decimal_places=0, max_digits=13)),
                ('prevBalance', models.DecimalField(db_column='tranPrevBalance', decimal_places=0, max_digits=13)),
                ('postBalance', models.DecimalField(db_column='tranPostBalance', decimal_places=0, max_digits=13)),
                ('prevFrozen', models.DecimalField(db_column='tranPrevFrozen', decimal_places=0, max_digits=13)),
                ('postFrozen', models.DecimalField(db_column='tranPostFrozen', decimal_places=0, max_digits=13)),
                ('flow', models.CharField(choices=[('I', 'Inflow'), ('O', 'Outflow'), ('F', 'Infreeze'), ('U', 'Outfreeze')], db_column='tranFlow', max_length=1)),
                ('account', models.ForeignKey(db_column='usrId', on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transactions.account')),
                ('admin', models.ForeignKey(db_column='admId', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='users_auth.admin')),
                ('offer', models.ForeignKey(db_column='offId', null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.offer')),
                ('payment', models.OneToOneField(db_column='payId', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='transactions.payment')),
            ],
            options={
                'db_table': 'TRANSACTION',
            },
        ),
    ]
