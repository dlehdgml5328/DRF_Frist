import os
import json
from django.conf import settings
from django.http import JsonResponse


# JSON 파일 불러오기 함수
def load_json_file():
    file_path = os.path.join(settings.BASE_DIR, "sales_data.json")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def monthly_sales_summary(request):
    data = load_json_file()
    result = {}

    for item in data:
        month = item["order_date"][:7] + "-01"
        sales = item["price"] * item["quantity"]

        if month in result:
            result[month] += sales
        else:
            result[month] = sales

    response_data = []
    for month, total in sorted(result.items()):
        response_data.append({"month": month, "total_sales": total})

    return JsonResponse(response_data, safe=False)


def category_sales_summary(request):
    data = load_json_file()
    result = {}

    for item in data:
        category = item["category"]
        sales = item["price"] * item["quantity"]

        if category in result:
            result[category] += sales
        else:
            result[category] = sales

    response_data = []
    for category, total in sorted(result.items()):
        response_data.append({"category": category, "total_sales": total})

    return JsonResponse(response_data, safe=False)
