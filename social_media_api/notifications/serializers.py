from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['recipient', 'actor', 'verb', 'target', 'timestamp']
        read_only_fields = ['recipent', 'actor', 'verb', 'target','timestamp']

    def get_target(self, obj):
        if obj.target:
            return f"{obj.target_content_type.model} {obj.target_object_id}"
        return None