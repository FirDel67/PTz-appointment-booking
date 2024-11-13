[1mdiff --git a/.gitignore b/.gitignore[m
[1mdeleted file mode 100644[m
[1mindex 82f9275..0000000[m
[1m--- a/.gitignore[m
[1m+++ /dev/null[m
[36m@@ -1,162 +0,0 @@[m
[31m-# Byte-compiled / optimized / DLL files[m
[31m-__pycache__/[m
[31m-*.py[cod][m
[31m-*$py.class[m
[31m-[m
[31m-# C extensions[m
[31m-*.so[m
[31m-[m
[31m-# Distribution / packaging[m
[31m-.Python[m
[31m-build/[m
[31m-develop-eggs/[m
[31m-dist/[m
[31m-downloads/[m
[31m-eggs/[m
[31m-.eggs/[m
[31m-lib/[m
[31m-lib64/[m
[31m-parts/[m
[31m-sdist/[m
[31m-var/[m
[31m-wheels/[m
[31m-share/python-wheels/[m
[31m-*.egg-info/[m
[31m-.installed.cfg[m
[31m-*.egg[m
[31m-MANIFEST[m
[31m-[m
[31m-# PyInstaller[m
[31m-#  Usually these files are written by a python script from a template[m
[31m-#  before PyInstaller builds the exe, so as to inject date/other infos into it.[m
[31m-*.manifest[m
[31m-*.spec[m
[31m-[m
[31m-# Installer logs[m
[31m-pip-log.txt[m
[31m-pip-delete-this-directory.txt[m
[31m-[m
[31m-# Unit test / coverage reports[m
[31m-htmlcov/[m
[31m-.tox/[m
[31m-.nox/[m
[31m-.coverage[m
[31m-.coverage.*[m
[31m-.cache[m
[31m-nosetests.xml[m
[31m-coverage.xml[m
[31m-*.cover[m
[31m-*.py,cover[m
[31m-.hypothesis/[m
[31m-.pytest_cache/[m
[31m-cover/[m
[31m-[m
[31m-# Translations[m
[31m-*.mo[m
[31m-*.pot[m
[31m-[m
[31m-# Django stuff:[m
[31m-*.log[m
[31m-local_settings.py[m
[31m-db.sqlite3[m
[31m-db.sqlite3-journal[m
[31m-[m
[31m-# Flask stuff:[m
[31m-instance/[m
[31m-.webassets-cache[m
[31m-[m
[31m-# Scrapy stuff:[m
[31m-.scrapy[m
[31m-[m
[31m-# Sphinx documentation[m
[31m-docs/_build/[m
[31m-[m
[31m-# PyBuilder[m
[31m-.pybuilder/[m
[31m-target/[m
[31m-[m
[31m-# Jupyter Notebook[m
[31m-.ipynb_checkpoints[m
[31m-[m
[31m-# IPython[m
[31m-profile_default/[m
[31m-ipython_config.py[m
[31m-[m
[31m-# pyenv[m
[31m-#   For a library or package, you might want to ignore these files since the code is[m
[31m-#   intended to run in multiple environments; otherwise, check them in:[m
[31m-# .python-version[m
[31m-[m
[31m-# pipenv[m
[31m-#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.[m
[31m-#   However, in case of collaboration, if having platform-specific dependencies or dependencies[m
[31m-#   having no cross-platform support, pipenv may install dependencies that don't work, or not[m
[31m-#   install all needed dependencies.[m
[31m-#Pipfile.lock[m
[31m-[m
[31m-# poetry[m
[31m-#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.[m
[31m-#   This is especially recommended for binary packages to ensure reproducibility, and is more[m
[31m-#   commonly ignored for libraries.[m
[31m-#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control[m
[31m-#poetry.lock[m
[31m-[m
[31m-# pdm[m
[31m-#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.[m
[31m-#pdm.lock[m
[31m-#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it[m
[31m-#   in version control.[m
[31m-#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control[m
[31m-.pdm.toml[m
[31m-.pdm-python[m
[31m-.pdm-build/[m
[31m-[m
[31m-# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm[m
[31m-__pypackages__/[m
[31m-[m
[31m-# Celery stuff[m
[31m-celerybeat-schedule[m
[31m-celerybeat.pid[m
[31m-[m
[31m-# SageMath parsed files[m
[31m-*.sage.py[m
[31m-[m
[31m-# Environments[m
[31m-.env[m
[31m-.venv[m
[31m-env/[m
[31m-venv/[m
[31m-ENV/[m
[31m-env.bak/[m
[31m-venv.bak/[m
[31m-[m
[31m-# Spyder project settings[m
[31m-.spyderproject[m
[31m-.spyproject[m
[31m-[m
[31m-# Rope project settings[m
[31m-.ropeproject[m
[31m-[m
[31m-# mkdocs documentation[m
[31m-/site[m
[31m-[m
[31m-# mypy[m
[31m-.mypy_cache/[m
[31m-.dmypy.json[m
[31m-dmypy.json[m
[31m-[m
[31m-# Pyre type checker[m
[31m-.pyre/[m
[31m-[m
[31m-# pytype static type analyzer[m
[31m-.pytype/[m
[31m-[m
[31m-# Cython debug symbols[m
[31m-cython_debug/[m
[31m-[m
[31m-# PyCharm[m
[31m-#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can[m
[31m-#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore[m
[31m-#  and can be added to the global gitignore or merged into this file.  For a more nuclear[m
[31m-#  option (not recommended) you can uncomment the following to ignore the entire idea folder.[m
[31m-#.idea/[m
[1mdiff --git a/App/__init__.py b/App/__init__.py[m
[1mnew file mode 100644[m
[1mindex 0000000..e69de29[m
[1mdiff --git a/App/__pycache__/__init__.cpython-311.pyc b/App/__pycache__/__init__.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..7e0b2f0[m
Binary files /dev/null and b/App/__pycache__/__init__.cpython-311.pyc differ
[1mdiff --git a/App/__pycache__/admin.cpython-311.pyc b/App/__pycache__/admin.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..c0a36e5[m
Binary files /dev/null and b/App/__pycache__/admin.cpython-311.pyc differ
[1mdiff --git a/App/__pycache__/apps.cpython-311.pyc b/App/__pycache__/apps.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..2021966[m
Binary files /dev/null and b/App/__pycache__/apps.cpython-311.pyc differ
[1mdiff --git a/App/__pycache__/forms.cpython-311.pyc b/App/__pycache__/forms.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..4ff5b6f[m
Binary files /dev/null and b/App/__pycache__/forms.cpython-311.pyc differ
[1mdiff --git a/App/__pycache__/models.cpython-311.pyc b/App/__pycache__/models.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..b026e2b[m
Binary files /dev/null and b/App/__pycache__/models.cpython-311.pyc differ
[1mdiff --git a/App/__pycache__/urls.cpython-311.pyc b/App/__pycache__/urls.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..26f6cd2[m
Binary files /dev/null and b/App/__pycache__/urls.cpython-311.pyc differ
[1mdiff --git a/App/__pycache__/views.cpython-311.pyc b/App/__pycache__/views.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..da05b0a[m
Binary files /dev/null and b/App/__pycache__/views.cpython-311.pyc differ
[1mdiff --git a/App/admin.py b/App/admin.py[m
[1mnew file mode 100644[m
[1mindex 0000000..02ae715[m
[1m--- /dev/null[m
[1m+++ b/App/admin.py[m
[36m@@ -0,0 +1,11 @@[m
[32m+[m[32mfrom django.contrib import admin[m
[32m+[m
[32m+[m[32mfrom .models import *[m
[32m+[m
[32m+[m[32m# Register your models here.[m
[32m+[m
[32m+[m[32madmin.site.register(CustomUser)[m
[32m+[m[32madmin.site.register(Clinic)[m
[32m+[m[32madmin.site.register(Doctor)[m
[32m+[m[32madmin.site.register(Availability)[m
[32m+[m[32madmin.site.register(Appointment)[m
\ No newline at end of file[m
[1mdiff --git a/App/apps.py b/App/apps.py[m
[1mnew file mode 100644[m
[1mindex 0000000..9df3b1c[m
[1m--- /dev/null[m
[1m+++ b/App/apps.py[m
[36m@@ -0,0 +1,6 @@[m
[32m+[m[32mfrom django.apps import AppConfig[m
[32m+[m
[32m+[m
[32m+[m[32mclass AppConfig(AppConfig):[m
[32m+[m[32m    default_auto_field = 'django.db.models.BigAutoField'[m
[32m+[m[32m    name = 'App'[m
[1mdiff --git a/App/forms.py b/App/forms.py[m
[1mnew file mode 100644[m
[1mindex 0000000..fd813e6[m
[1m--- /dev/null[m
[1m+++ b/App/forms.py[m
[36m@@ -0,0 +1,15 @@[m
[32m+[m[32mfrom django import forms[m
[32m+[m[32mfrom .models import CustomUser[m
[32m+[m
[32m+[m[32mclass UpdatePatientForm(forms.ModelForm):[m
[32m+[m[32m    class Meta:[m
[32m+[m[32m        model = CustomUser[m
[32m+[m[32m        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'username'][m
[32m+[m[32m        widgets = {[m
[32m+[m[32m            'first_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),[m
[32m+[m[32m            'last_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),[m
[32m+[m[32m            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),[m
[32m+[m[32m            'phone_number': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),[m
[32m+[m[32m            'address': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),[m
[32m+[m[32m            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),[m
[32m+[m[32m        }[m
[1mdiff --git a/App/migrations/0001_initial.py b/App/migrations/0001_initial.py[m
[1mnew file mode 100644[m
[1mindex 0000000..c904053[m
[1m--- /dev/null[m
[1m+++ b/App/migrations/0001_initial.py[m
[36m@@ -0,0 +1,129 @@[m
[32m+[m[32m# Generated by Django 5.1.1 on 2024-11-05 06:20[m
[32m+[m
[32m+[m[32mimport django.contrib.auth.models[m
[32m+[m[32mimport django.db.models.deletion[m
[32m+[m[32mimport django.utils.timezone[m
[32m+[m[32mimport uuid[m
[32m+[m[32mfrom django.conf import settings[m
[32m+[m[32mfrom django.db import migrations, models[m
[32m+[m
[32m+[m
[32m+[m[32mclass Migration(migrations.Migration):[m
[32m+[m
[32m+[m[32m    initial = True[m
[32m+[m
[32m+[m[32m    dependencies = [[m
[32m+[m[32m        ('auth', '0012_alter_user_first_name_max_length'),[m
[32m+[m[32m    ][m
[32m+[m
[32m+[m[32m    operations = [[m
[32m+[m[32m        migrations.CreateModel([m
[32m+[m[32m            name='Clinic',[m
[32m+[m[32m            fields=[[m
[32m+[m[32m                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),[m
[32m+[m[32m                ('name', models.CharField(max_length=100)),[m
[32m+[m[32m                ('address', models.CharField(max_length=255)),[m
[32m+[m[32m                ('phone', models.CharField(max_length=15)),[m
[32m+[m[32m                ('email', models.EmailField(max_length=254)),[m
[32m+[m[32m                ('description', models.TextField(blank=True, null=True)),[m
[32m+[m[32m                ('opening_hours', models.CharField(blank=True, max_length=100, null=True)),[m
[32m+[m[32m            ],[m
[32m+[m[32m        ),[m
[32m+[m[32m        migrations.CreateModel([m
[32m+[m[32m            name='Doctor',[m
[32m+[m[32m            fields=[[m
[32m+[m[32m                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),[m
[32m+[m[32m                ('first_name', models.CharField(max_length=100)),[m
[32m+[m[32m                ('last_name', models.CharField(max_length=100)),[m
[32m+[m[32m                ('specialty', models.CharField(max_length=100)),[m
[32m+[m[32m                ('email', models.EmailField(max_length=254)),[m
[32m+[m[32m                ('created_at', models.DateTimeField(auto_now_add=True)),[m
[32m+[m[32m                ('updated_at', models.DateTimeField(auto_now=True)),[m
[32m+[m[32m                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='App.clinic')),[m
[32m+[m[32m            ],[m
[32m+[m[32m        ),[m
[32m+[m[32m        migrations.CreateModel([m
[32m+[m[32m            name='Appointment',[m
[32m+[m[32m            fields=[[m
[32m+[m[32m                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),[m
[32m+[m[32m                ('date', models.DateField()),[m
[32m+[m[32m                ('time', models.TimeField()),[m
[32m+[m[32m                ('ticket_id', models.UUIDField()),[m
[32m+[m[32m                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=50)),[m
[32m+[m[32m                ('canceled_at', models.DateTimeField(blank=True, null=True)),[m
[32m+[m[32m                ('rescheduled_at', models.DateTimeField(blank=True, null=True)),[m
[32m+[m[32m                ('created_at', models.DateTimeField(auto_now_add=True)),[m
[32m+[m[32m                ('updated_at', models.DateTimeField(auto_now=True)),[m
[32m+[m[32m                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_appointments', to='App.clinic')),[m
[32m+[m[32m                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dr_appointments', to='App.doctor')),[m
[32m+[m[32m            ],[m
[32m+[m[32m        ),[m
[32m+[m[32m        migrations.CreateModel([m
[32m+[m[32m            name='Ticket',[m
[32m+[m[32m            fields=[[m
[32m+[m[32m                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),[m
[32m+[m[32m                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),[m
[32m+[m[32m                ('issued_at', models.DateTimeField(auto_now_add=True)),[m
[32m+[m[32m                ('qr_code', models.ImageField(blank=True, null=True, upload_to='tickets/')),[m
[32m+[m[32m                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='App.appointment')),[m
[32m+[m[32m            ],[m
[32m+[m[32m        ),[m
[32m+[m[32m        migrations.CreateModel([m
[32m+[m[32m            name='CustomUser',[m
[32m+[m[32m            fields=[[m
[32m+[m[32m                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),[m
[32m+[m[32m                ('password', models.CharField(max_length=128, verbose_name='password')),[m
[32m+[m[32m                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),[m
[32m+[m[32m                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),[m
[32m+[m[32m                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),[m
[32m+[m[32m                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),[m
[32m+[m[32m                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),[m
[32m+[m[32m                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),[m
[32m+[m[32m                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),[m
[32m+[m[32m                ('phone_number', models.BigIntegerField()),[m
[32m+[m[32m                ('username', models.CharField(blank=True, max_length=255, null=True)),[m
[32m+[m[32m                ('email', models.EmailField(max_length=254, unique=True)),[m
[32m+[m[32m                ('birth_date', models.DateField(blank=True, null=True)),[m
[32m+[m[32m                ('address', models.TextField(blank=True, null=True)),[m
[32m+[m[32m                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),[m
[32m+[m[32m                ('profile', models.ImageField(blank=True, null=True, upload_to='profile_images/')),[m
[32m+[m[32m                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),[m
[32m+[m[32m                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permis