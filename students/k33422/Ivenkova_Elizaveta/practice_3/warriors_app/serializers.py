from rest_framework import serializers
from warriors_app import models




class WarriorSerializer(serializers.ModelSerializer):
    # practice 3.2 пункт 3 пример
    class Meta:
        model = models.Warrior
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    # практика 3.2 Пункт 3
    # Вывод и созданеи скилла
    """
    Можем использовать как для get, так и для post
    """
    class Meta:
        model = models.Skill
        fields = '__all__'

class ProfessionCreateSerializer(serializers.Serializer):
    # практкика 3.2  Пункт 4 пример
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    # Переопределяем только его, потому что save более высокого уровня
    def create(self, validated_data):
        # validated_data - словарь, поэтому **
        prof_model_inst = models.Profession(**validated_data)
        prof_model_inst.save()
        return prof_model_inst

    def update(self, instance, validated_data):
        pass

class ProfessionSerializer(serializers.ModelSerializer):
    # практкика 3.2  Пункт 4 пример
    class Meta:
        model = models.Profession
        fields = '__all__'


class SkillRelatedSerializer(serializers.ModelSerializer):
    # практкика 3.2  Пункт 4 пример
    warrior = WarriorSerializer(many=True)

    class Meta:
        model = models.Skill
        fields = '__all__'


class WarriorRelatedSerializer(serializers.ModelSerializer):
    # практкика 3.2  Пункт 4 пример
    skill = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    class Meta:
        model=models.Warrior
        fields = '__all__'


class WarriorDepthSerializer(serializers.ModelSerializer):
    # практкика 3.2  Пункт 4 пример
    class Meta:
        model = models.Warrior
        fields = '__all__'
        depth = 1

class WarriorNestedSerializer(serializers.ModelSerializer):
    # практкика 3.2  Пункт 4 пример
    profession = ProfessionSerializer(many=False, read_only=True)
    skill = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = models.Warrior
        fields = '__all__'

class WarriorProfessionSerializer(serializers.ModelSerializer):
    # практкиа 3.2 пункт 4
    # Вывод полной информации о всех войнах и профессии(в одном запросе).
    profession = ProfessionSerializer(many=False, read_only=True)

    class Meta:
        model = models.Warrior
        fields = '__all__'


class WarriorSkillSerializer(serializers.ModelSerializer):
    # практкиа 3.2 пункт 4
    # Вывод полной информации о всех войнах и их скилах (в одном запросе).
    skill = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = models.Warrior
        fields = '__all__'


class ProfessionWithWarriorSerializer(serializers.ModelSerializer):
    warrior = WarriorSerializer(many=True, read_only=True)
    class Meta:
        model = models.Profession
        fields = ['title', 'description', 'warrior']









