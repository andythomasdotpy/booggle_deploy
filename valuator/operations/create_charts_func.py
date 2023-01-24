import plotly.express as px
import plotly.io as pio
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import mplcursors


def scatter_plot_function(x, y, sales_data_list):
    fig1 = px.scatter(
        x=x,
        y=y,  
        title=sales_data_list,
        labels={"x": "Date" , "y": "Price ($usd)"}
    )

    fig1.update_layout(autotypenumbers='convert types')

    chart_1 = fig1.to_html()
    return chart_1


def line_chart_function(x, y, title):
    data = [dict(
            type='scatter',
            x=x,
            y=y,
            labels={"x": "Date"},
            mode='markers+lines',
            transforms=[dict(
                type='aggregate',
                groups=x,
                aggregations=[dict(
                    target='y',
                    func='avg',
                    enabled=True
                )]
            )]
        )]

    layout = dict(
        title = f'{title}',
        xaxis = dict(title = 'Date'),
        yaxis = dict(title = 'Price ($usd)'),
        autotypenumbers='convert types',
        tickangle=90
    )

    line_chart_agg = dict(
        data=data, 
        layout=layout
        )

    chart_2 = pio.to_html(line_chart_agg, validate=False)
    return chart_2


def seaborn_chart(x, y, title):
    print(x)
    d = {'sales_date': x, 'price_usd': y}

    print(d)

    df = pd.DataFrame(d, columns=['sales_date', 'price_usd'])
    print(df)


    # # Create chart and print to screen
    sns.set(rc={'figure.figsize': (12, 6)})
    sns.lineplot(data=df, x="sales_date", y="price_usd")
    sns.scatterplot(data=df, x="sales_date", y="price_usd")
    plt.xlabel('Date of Sale')
    plt.ylabel('Price (converted to USD)')
    # plt.xticks(rotation=295)
    mplcursors.cursor(hover=True)
    chart_3 = plt.to_html()
    # plt.savefig('books_read.png')
    return chart_3