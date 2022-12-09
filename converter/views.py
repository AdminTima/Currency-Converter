from django.shortcuts import render
from .utils import get_result
from .api import api_currency_list


def index(request):
    result = None
    context = {"result": result, "currency_list": api_currency_list}
    if request.method == "POST":
        from_currency = request.POST["from_currency"]
        to_currency = request.POST["to_currency"]
        amount_of_money = request.POST["amount_of_money"]
        result = get_result(from_currency, to_currency, amount_of_money)
        if result:
            context["result"] = result
        else:
            context["result"] = "Sorry an error occurred"

    return render(request, "converter/index.html", context)
