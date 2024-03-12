from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from warriors_app import serializers, models, filters



class WarriorAPIView(APIView):
    # пракатик 3.2 пункт 3 пример
    def get(self, request):
        warriors_query = filters.WarriorNameFilter(request.GET).qs
        warriors_serialized = serializers.WarriorRelatedSerializer(warriors_query,
                                                                   many=True)
        return Response({'warriors': warriors_serialized.data}, status=200)

class SkillApiView(APIView):
    # практика 3.2 Пункт 3
    # просмотр скиллов
    def get(self, request):
        skills_query = models.Skill.objects.all()
        skills_serialized = serializers.Skil(skills_query,
                                             many=True)
        return Response(skills_serialized.data)



class SkillCreateView(APIView):
    # практика 3.2 Пункт 3
    # создание скиллов
    def post(self, request):
        skill_dict = request.data.get('skill')
        skill_serialized = serializers.SkillSerializer(data=skill_dict)
        if skill_serialized.is_valid(raise_exception=True):
            skill_obj = skill_serialized.save()
        return Response({'Success': f'Skill {skill_obj.title} created'})


class ProfessionCreateView(APIView):
    # практкиа 3.2 пункт 4 пример
    def post(self, request):
        # Получаем из json данные под заголовком profession
        # Используем get, чтобы в случае если profession нет в словаре,
        # вернулось None
        prof_data = request.data.get('profession')
        prof_serializer = serializers.ProfessionCreateSerializer(data=prof_data)
        if prof_serializer.is_valid(raise_exception=True):
            prof_model_inst = prof_serializer.save()
        return Response({'Success': f'Profession {prof_model_inst.title} created'})



class WarriorAuthenticatedOnly(generics.ListAPIView):
    serializer_class = serializers.WarriorRelatedSerializer
    queryset = models.Warrior.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class WarriorWithProfessionView(generics.ListAPIView):
    # практика 3.2 пункт 4
    # Вывод полной информации о всех войнах и их профессиях (в одном запросе).
    serializer_class = serializers.WarriorProfessionSerializer
    filterset_class = filters.WarriorNameFilter

    def get_queryset(self):
        return models.Warrior.objects.filter(race='s')


class WarriorWithSkillView(generics.ListAPIView):
    # практика 3.2 пункт 4
    # Вывод полной информации о всех войнах и их скилах (в одном запросе).
    serializer_class = serializers.WarriorSkillSerializer
    queryset = models.Warrior.objects.all()

class WarriorRetrieveApiView(generics.RetrieveAPIView):
    # практика 3.2 пункт 4
    # Вывод полной информации о войне (по id), его профессиях и скилах.
    serializer_class = serializers.WarriorNestedSerializer
    queryset = models.Warrior.objects.all()

class WarriorRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    # практика 3.2 пункт 4
    # Удаление и редактирование воина по ID
    serializer_class = serializers.WarriorSerializer
    queryset = models.Warrior.objects.all()



class WarriorCreateApiView(generics.CreateAPIView):
    # Если поле проходит через вложенный serializer, то оно не отображается
    # в полях. Аналогично и с depth
    serializer_class = serializers.WarriorSerializer
    queryset = models.Warrior.objects.all()


class ProfessionApiView(APIView):
    def get(self, request):
        profession_query = models.Profession.objects.all()
        profession_serializer = serializers.ProfessionWithWarriorSerializer(profession_query,
                                                            many=True)
        return Response({'professions': profession_serializer.data}, status=200)


class SkillWithWarrior(APIView):
    def get(self, request):
        skills_query = models.Skill.objects.all()
        skills_serialized = serializers.SkillRelatedSerializer(skills_query,
                                                               many=True)
        return Response(skills_serialized.data)


