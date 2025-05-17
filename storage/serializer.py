from rest_framework import serializers
from storage.models import Storage, Size, Color

class StorageSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()

    def get_size(self, obj):
        return ",".join(size.name for size in obj.size.all())
    
    def get_color(self, obj):
        return ",".join(color.name for color in obj.color.all())

    class Meta:
        model = Storage
        fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"