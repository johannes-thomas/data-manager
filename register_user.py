from django.contrib.auth import get_user_model

user = get_user_model().objects.create_user(username='admin', email='johannes.thomas@slub-dresden.de', password='admin', is_staff=1, is_superuser=1)