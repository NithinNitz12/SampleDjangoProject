from rest_framework import serializers
from details.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id','Name','Age','Address','Email','Mob_no','City','Current_Designation']
