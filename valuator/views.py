from datetime import date
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View, TemplateView

from.models import SearchInput, ActualBottle
from .operations.bot_search_results import bot_find_search_results
from .operations.bot_scrape_data import bottle_results_bot
from .operations.create_charts_func import scatter_plot_function, line_chart_function, seaborn_chart

# Create your views here.


def search(request):
    # return HttpResponse("You are at home...")
    return render(request, "valuator/search.html")


class SearchResultsView(View):
    def post(self, request):
        search_entered = request.POST.get("search_box")

        # Add search term to database
        search = SearchInput()
        search.user_input = search_entered.title()
        search.date_created = date.today()
        search.save()

        search_bot_list = bot_find_search_results(search_entered)

        # Sort algo credited to @dimay: https://stackoverflow.com/questions/65679123/sort-nested-list-data-in-python
        search_bot_list_sorted = sorted(search_bot_list, key=lambda x: x[1], reverse=True)
        context = {"search_bot_list": search_bot_list_sorted}

        if len(search_bot_list) == 0:
            return render(request, "valuator/no_results_find.html", context)

        return render(request, "valuator/search_results.html", context)


class BottleDetailsView(View):
    def post(self, request):
        search_term = request.POST.get("bottle_name")

        sales_data_list = bottle_results_bot(search_term)

        # Add actual bottle lookup to database
        actual = ActualBottle()
        actual.actual_bottle = search_term.title()
        actual.photo_url = sales_data_list[0][3]
        actual.date_created = datetime.now()
        actual.save()

        x = [date[2] for date in sales_data_list]
        y = [price[1] for price in sales_data_list]

        x.reverse()
        y.reverse()

        # Create Scatter Plot
        chart_1 = scatter_plot_function(x, y, sales_data_list[0][0])

        # Create Aggregated Line Chart
        chart_2 = line_chart_function(x, y, search_term)

        # chart_3 = seaborn_chart(x, y, sales_data_list[0][0])

        context = {"sales_data_list": sales_data_list, "chart_1": chart_1, "chart": chart_2}

        return render(request, "valuator/bottle_details.html", context)


def trending(request):
    all_bottles = ActualBottle.objects.all().order_by('-date_created')
    print(all_bottles)
    
    dict_5_no_dups = dict()

    for bottles in all_bottles:
        dict_5_no_dups[bottles.actual_bottle] = bottles.photo_url
        if len(dict_5_no_dups) >= 4:
            break

    print()
    print()
    for key in dict_5_no_dups:
        print(key, dict_5_no_dups[key])


    context = {"all_bottles": dict_5_no_dups}

    # return render(request, "valuator/trending.html", context=context)
    return render(request, "valuator/index.html", context=context)



def bottle_details_trending(request, mid):
    print(mid)
    sales_data_list = bottle_results_bot(mid)

    # Add actual bottle lookup to database
    actual = ActualBottle()
    actual.actual_bottle = mid.title()
    actual.photo_url = sales_data_list[0][3]
    actual.date_created = datetime.now()
    actual.save()

    x = [date[2] for date in sales_data_list]
    y = [price[1] for price in sales_data_list]

    x.reverse()
    y.reverse()

    # Create Scatter Plot
    chart_1 = scatter_plot_function(x, y, sales_data_list[0][0])

    # Create Aggregated Line Chart
    chart_2 = line_chart_function(x, y, mid)

    # chart_3 = seaborn_chart(x, y, mid)

    context = {"sales_data_list": sales_data_list, "chart_1": chart_1, "chart": chart_2}

    return render(request, "valuator/bottle_details.html", context)


def popular(request):
    return render(request, "valuator/popular.html")


def search_results_popular(request, popular):
    print(popular)
    # Add search term to database
    search = SearchInput()
    search.user_input = popular.title()
    search.date_created = date.today()
    search.save()

    search_bot_list = bot_find_search_results(popular)

    # Sort algo credited to @dimay: https://stackoverflow.com/questions/65679123/sort-nested-list-data-in-python
    search_bot_list_sorted = sorted(search_bot_list, key=lambda x: x[1], reverse=True)
    context = {"search_bot_list": search_bot_list_sorted}

    if len(search_bot_list) == 0:
        return render(request, "valuator/no_results_find.html", context)

    return render(request, "valuator/search_results.html", context)


class PostTemplateView(TemplateView):
    template_name = "valuator/spinner.html"