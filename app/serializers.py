from swampdragon.serializers.model_serializer import ModelSerializer

class NotificationSerializer(ModelSerializer):
	class Meta:
		model = 'app.Notification'
		publish_fields = ['message']