from rest_framework import serializers
from .models import Project, Pledge, ProjectUpdates, LikedBy
# from users.models import CustomUser
# from users.serializers import CustomUserSerializer


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.DecimalField(max_digits=10, decimal_places=2)
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner_id')
    total = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter', 'date_created']
        read_only_fields = ['id', 'supporter']

class ProjectUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUpdates
        fields = ['id', 'content', 'project', 'date_created']


class LikedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedBy
        fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = LikedBySerializer(many=True, read_only=True)
    projectupdates = ProjectUpdatesSerializer(many=True, read_only=True)


