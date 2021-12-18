import datetime
import json

from django.http import JsonResponse
from rest_framework.views import APIView

from table_task.models import TaskTable
from table_task.serializers import TableSerializer


class TableView(APIView):
    def get(self, request):
        try:
            col = request.GET["col"]
            logic = request.GET["logic"]
            value = request.GET["value"]
        except KeyError:
            col = ""
            logic = ""
            value = ""
        limit = int(request.GET["limit"])
        offset = int(request.GET["offset"])

        table = TaskTable.objects.all()
        if col and logic and value:
            table = table.filter(**self.prepare_filtering_request(col, logic, value))

        total = len(table)
        table = table[offset : offset + limit]
        serialized_table = TableSerializer(table, many=True).data
        return JsonResponse({"table": serialized_table, "total": total}, status=200)

    def prepare_filtering_request(self, col, logic, value):
        logic_map = {
            "equal": "__exact",
            "more": "__gt",
            "less": "__lt",
            "contains": "__contains",
        }
        key = f"{col}{logic_map[logic]}"
        return {key: value}


class TablePost(APIView):
    def post(self, request):
        date = request.data["date"]
        name = request.data["name"]
        quantity = request.data["quantity"]
        distance = request.data["distance"]

        table = TaskTable(date=date, name=name, quantity=quantity, distance=distance)
        table.save()

        return JsonResponse({"success": "successfully created"}, status=200)
