from rest_framework import serializers
from .models import ModelFAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModelFAQ
        field=['id','question','answer','keywords']