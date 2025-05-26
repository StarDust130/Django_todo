from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    extra_info = serializers.SerializerMethodField()  # Send extra_info with output

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed',
                  'created_at', 'updated_at', 'extra_info']
        read_only_fields = ['created_at', 'updated_at']

    # Cal extra_info 
    def get_extra_info(self, obj):
        return f"Created at {obj.created_at.strftime('%d-%m-%Y')}"

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters.")
        return value


