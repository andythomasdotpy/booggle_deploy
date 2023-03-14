from datetime import date
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View, TemplateView


from .forms import UserRegistrationForm
from .models import SearchInput, ActualBottle
from .operations.bot_search_results import bot_find_search_results
from .operations.bot_scrape_data import bottle_results_bot
from .operations.create_charts_func import scatter_plot_function, line_chart_function, seaborn_chart

# Create your views here.


def search(request):
    # return HttpResponse("You are at home...")
    all_bottles = ActualBottle.objects.all().order_by('-date_created')
    single_bottle = all_bottles[:1][0]
    print(single_bottle.photo_url)
    
    context = {"single_bottle": single_bottle}

    return render(request, "valuator/search.html", context)


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
        if len(dict_5_no_dups) >= 8:
            break

    print()
    print()
    for key in dict_5_no_dups:
        print(key, dict_5_no_dups[key])


    context = {"all_bottles": dict_5_no_dups}

    # return render(request, "valuator/trending.html", context=context)
    return render(request, "valuator/trending.html", context=context)



def bottle_details_trending(request, mid):
    print(mid)
    sales_data_list = bottle_results_bot(mid)

    # Add actual bottle lookup to database
    actual = ActualBottle()
    print(actual)
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


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            # Create new user object but don't save yet. Check passwords.
            new_user = user_form.save(commit=False)

            # Set password
            new_user.set_password(user_form.cleaned_data["password_1"])
            new_user.save()
            content = {"user_form": user_form}

            return render(request, "account/register_done.html", content)

    else:
        user_form = UserRegistrationForm()
        {"user_form": user_form}

    return render(request, "account/register.html", {"user_form": user_form})


def favorites(request):
    # # Obtain logged in user_id
    # loggedin_user = request.user.id

    # # Query for all likes associated with user_id
    # posts_liked_by_user = Likes.objects.filter(user_id=loggedin_user)

    # # Create blank list to add posts liked by user
    # posts_list = list()

    # # Iterate through likes, search if like is associated with logged in user, create list of dicts adding liked date from likes table to user info
    # for like in posts_liked_by_user:
    #     tmp_dict = dict()
    #     try:
    #         single_post = Post.objects.get(pk=like.post_id)

    #         tmp_dict["id"] = single_post.id
    #         tmp_dict["title"] = single_post.title
    #         tmp_dict["author"] = single_post.author
    #         tmp_dict["slug"] = single_post.slug
    #         tmp_dict["image"] = single_post.image
    #         tmp_dict["date_time_like"] = like.date
    #         posts_list.append(tmp_dict)
    #     except:
    #         pass
    
    # sorted_list_by_liked_date = sorted(posts_list, reverse=True, key=lambda d: d['date_time_like']) 

    # context = {"posts_list": sorted_list_by_liked_date}
    context = {}


    return render(request, "valuator/favorites.html", context)


def favorites_add(request):
    # Obtain User Id
    # Obtain Post Id
    # Add new row to likes table with post id and user id
    # 
    return redirect("search")