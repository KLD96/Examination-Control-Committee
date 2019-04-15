# Generated by Django 2.1.2 on 2019-04-05 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_member', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('CCollege', models.IntegerField(primary_key=True, serialize=False, verbose_name='College Code')),
                ('Cname', models.CharField(max_length=160, verbose_name='College Name')),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(choices=[('invigilator', 'Invigilator')], max_length=60, verbose_name='Role')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CoCourse', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Course Code')),
                ('CoName', models.CharField(max_length=255, verbose_name='Course Name')),
                ('Level', models.CharField(choices=[('Fi', 'First'), ('SE', 'Seconed'), ('TH', 'Third'), ('FO', 'Fourth'), ('FI', 'Fifth')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('Dcode', models.IntegerField(primary_key=True, serialize=False, verbose_name='Department Code')),
                ('Dname', models.CharField(max_length=255, verbose_name='Department Name')),
                ('CCollege', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.College', verbose_name='College Code')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('E_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='Exam ID')),
                ('Period', models.CharField(choices=[('First', '8:00 AM - 10:00 AM'), ('Seconed', '10:30 AM - 12:30 PM'), ('Third', '1:00 PM - 3:00 PM')], max_length=10)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Has',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Exam', verbose_name='Exam ID')),
            ],
        ),
        migrations.CreateModel(
            name='Inst_Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_number', models.CharField(max_length=14, unique=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('Ins_ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Instructor ID')),
                ('Fname', models.CharField(max_length=60, verbose_name='First Name')),
                ('Minit', models.CharField(max_length=60, null=True, verbose_name='Middle Name')),
                ('Lname', models.CharField(max_length=60, verbose_name='Last Name')),
                ('Rank', models.CharField(max_length=60)),
                ('Email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('Dcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Dept', verbose_name='Department Code')),
            ],
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, choices=[('forgitId', 'Forgit ID Report'), ('phone', 'Phone Report'), ('Cheating', 'Cheating Report')], default=None, max_length=15, null=True)),
                ('Describtion', models.TextField()),
                ('E_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Exam', verbose_name='Exam ID')),
                ('Ins_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Instructor', verbose_name='Instructor ID')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BLDG', models.CharField(max_length=60, verbose_name='Bulding Number')),
                ('Room', models.CharField(max_length=60)),
                ('Size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Section ID')),
                ('Name', models.CharField(max_length=60, verbose_name='Section Name')),
                ('Semester', models.CharField(max_length=60)),
                ('year', models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2019, verbose_name='year')),
                ('CCourse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Course', verbose_name='Course Code')),
                ('E_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Exam', verbose_name='Exam ID')),
                ('Ins_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Instructor', verbose_name='Instructor ID')),
            ],
        ),
        migrations.CreateModel(
            name='Std_Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_number', models.CharField(max_length=14, unique=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Std_ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='Student ID')),
                ('Fname', models.CharField(max_length=60, verbose_name='First Name')),
                ('Minit', models.CharField(max_length=60, verbose_name='Middle Name')),
                ('Lname', models.CharField(max_length=60, verbose_name='Last Name')),
                ('Dcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Dept', verbose_name='Department Code')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Status', models.BooleanField(default=False, verbose_name='Submission status')),
                ('D_Status', models.BooleanField(default=False, verbose_name='Delivery status')),
                ('ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Section', verbose_name='Section ID')),
                ('Ins_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Instructor', verbose_name='Instructor ID')),
                ('Member_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Member_ID+', to='main_app.Instructor', verbose_name='Examination Control Member ID')),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sec_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Section', verbose_name='Section ID')),
                ('Std_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Student', verbose_name='Student ID')),
            ],
        ),
        migrations.AddField(
            model_name='std_phone',
            name='Std_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Student', verbose_name='Student ID'),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('BLDG', 'Room')},
        ),
        migrations.AddField(
            model_name='problems',
            name='Std_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Student', verbose_name='Student ID'),
        ),
        migrations.AddField(
            model_name='inst_phone',
            name='Ins_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Instructor', verbose_name='Instructor ID'),
        ),
        migrations.AddField(
            model_name='has',
            name='Room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Room'),
        ),
        migrations.AddField(
            model_name='dept',
            name='Ins_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Instructor', verbose_name='Instructor ID'),
        ),
        migrations.AddField(
            model_name='course',
            name='Dcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Dept', verbose_name='Department Code'),
        ),
        migrations.AddField(
            model_name='control',
            name='E_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Exam', verbose_name='Exam ID'),
        ),
        migrations.AddField(
            model_name='control',
            name='Ins_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Instructor', verbose_name='Instructor ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='Ins_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Instructor', verbose_name='Instructor ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='takes',
            unique_together={('Std_ID', 'Sec_ID')},
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('CCourse', 'Ins_ID')},
        ),
        migrations.AlterUniqueTogether(
            name='has',
            unique_together={('Room', 'E_ID')},
        ),
        migrations.AlterUniqueTogether(
            name='control',
            unique_together={('Ins_ID', 'E_ID')},
        ),
    ]