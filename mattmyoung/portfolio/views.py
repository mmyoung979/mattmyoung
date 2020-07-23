# Django imports
from django.shortcuts import render

# Python imports
import plotly.express as px


# Portfolio Page
def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def pts(request):
    return render(request, 'portfolio/pts.html')

def plotly(request):
    data = px.data.gapminder()
    data_canada = data[data.country == 'Canada']
    fig = px.bar(data_canada,
                 x='year',
                 y='pop',
                 hover_data=['lifeExp', 'gdpPercap'],
                 color='lifeExp',
                 labels={'pop':'population of Canada'})
    graph = fig.to_html(full_html=False)
    context = {'graph': graph}
    return render(request, 'portfolio/plotly.html', context)
