from rest_framework import serializers 

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'titulo', 'descripcion', 'hecha')