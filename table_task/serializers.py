from rest_framework import serializers

from table_task.models import TaskTable


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTable
        fields = "__all__"


