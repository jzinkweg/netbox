# Generated by Django 4.1.7 on 2023-03-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0066_iprange_mark_utilized'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='fhrpgroupassignment',
            index=models.Index(fields=['interface_type', 'interface_id'], name='ipam_fhrpgr_interfa_2acc3f_idx'),
        ),
        migrations.AddIndex(
            model_name='ipaddress',
            index=models.Index(fields=['assigned_object_type', 'assigned_object_id'], name='ipam_ipaddr_assigne_890ab8_idx'),
        ),
        migrations.AddIndex(
            model_name='l2vpntermination',
            index=models.Index(fields=['assigned_object_type', 'assigned_object_id'], name='ipam_l2vpnt_assigne_bac7ae_idx'),
        ),
        migrations.AddIndex(
            model_name='vlangroup',
            index=models.Index(fields=['scope_type', 'scope_id'], name='ipam_vlangr_scope_t_9da557_idx'),
        ),
    ]
