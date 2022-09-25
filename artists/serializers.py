from rest_framework import serializers
from .models import Artist



class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reviews_count = serializers.ReadOnlyField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Artist
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'profile_image', 'speciality', 'hourly_rate', 'location',
            'created_at', 'updated_at', 'reviews_count',
        ]
