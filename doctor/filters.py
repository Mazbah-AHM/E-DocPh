import django_filters
from store.models import *


class doc_app(django_filters.FilterSet):
    class Meta:
        model = Prescription
        fields = '__all__'