from flask import Flask, render_template
import xmlrpc.client
import pandas as pd
from altair import Chart, X, Y, Axis, Data, DataFormat
import altair as alt
from vega_datasets import data
import pygeohash as pgh
from transport import RequestsTransport

app = Flask(__name__)
proxy = xmlrpc.client.ServerProxy('http://0.0.0.0:2228/', transport=RequestsTransport())

month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

height = 150
width = 250

@app.route("/")
def index():
    return render_template('./index.html')

@app.route('/corr/<this>/<that>')
def serve_corr(this, that):
    return str(proxy.summarizer.correlation_matrix.get_correlation(this, that))

@app.route('/max/<day>/<feature>')
def serve_max_for_day(day, feature):
    day = int(day)
    return str(proxy.summarizer.getMaxForDay(day, feature))

@app.route('/min/<day>/<feature>')
def serve_min_for_day(day, feature):
    day = int(day)
    return str(proxy.summarizer.getMinForDay(day, feature))

@app.route('/mean/<day>/<feature>')
def serve_mean_for_day(day, feature):
    day = int(day)
    return str(proxy.summarizer.getMeanForDay(day, feature))

@app.route('/variance/<day>/<feature>')
def serve_variance_for_day(day, feature):
    day = int(day)
    return str(proxy.summarizer.getVarianceForDay(day, feature))

@app.route('/showLocations')
def serve_unique_location():
    locations = proxy.summarizer.getUniqueLocation()
    return str(locations)

    # lat_long_vals = [pgh.decode(i) for i in locations]
    # d = pd.DataFrame(lat_long_vals)
    # states = alt.topo_feature(data.us_10m.url, 'states')
    #
    # # US states background
    # background = alt.Chart(states).mark_geoshape(
    #     fill='lightgray',
    #     stroke='white'
    # ).properties(
    #     title='US State Capitols',
    #     width=700,
    #     height=400
    # ).project('albersUsa')
    #
    # # Points and text
    # hover = alt.selection(type='single', on='mouseover', nearest=True,
    #                       fields=['lat', 'lon'])
    #
    # base = alt.Chart(d).encode(
    #     longitude='0:Q',
    #     latitude='1:Q'
    # )
    #
    # points = base.mark_point().encode(
    #     color=alt.value('black'),
    #     size=alt.condition(~hover, alt.value(30), alt.value(100))
    # ).add_selection(hover)
    #
    # return (background + points).to_json()



@app.route('/meanStats/<feature>')
def serve_mean_stats(feature):
    print(feature)
    result = proxy.summarizer.getMeanStats(feature)
    result_array = str(result).split()
    list_name = ['l' + str(x) for x in range(1, 367)]
    df_list = pd.DataFrame({'data': result_array, 'name': list_name})
    print(list_name)
    print(result_array)
    print("printing!!!")
    print(len(result_array), len(list_name))  # Print all of them out here

    chart = Chart(data=df_list, height=height, width=width).mark_bar(color='lightgreen').encode(
        X('name', axis=Axis(title='Sample')),
        Y('data', axis=Axis(title='Value'))
    )
    # return chart.to_json()
    return str(result)


@app.route('/varStats/<feature>')
def serve_var_stats(feature):
    result = proxy.summarizer.getvarStatsByMonth(feature)
    result_array = str(result).split()
    list_name = ['' + str(x) for x in range(1, 13)]
    df_list = pd.DataFrame({'data': result_array, 'name': list_name})

    chart = Chart(data=df_list, height=height, width=width).mark_bar(color='lightgreen').encode(
        X('name', axis=Axis(title='Sample')),
        Y('data', axis=Axis(title='Value'))
    )
    # return chart.to_json()
    return str(result)


@app.route('/maxStats/airTemp')
def serve_max_stats_air_temp():
    maxListByMonth_air_temp = proxy.summarizer.getMaxStatsByMonth('AIR_TEMPERATURE')
    print("max stats for air temp: " + str(maxListByMonth_air_temp))
    df_list = pd.DataFrame({'data': maxListByMonth_air_temp, 'name': month_lst})
    chart1 = Chart(data=df_list, height=height, width=width).mark_bar(color='blue').encode(
        X('name', axis=Axis(title='Month'), sort= None),
        Y('data', axis=Axis(title='Max'))
    )
    return chart1.to_json()

@app.route('/minStats/airTemp')
def serve_min_stats_air_temp():
    minListByMonth_air_temp = proxy.summarizer.getMinStatsByMonth('AIR_TEMPERATURE')
    print("min stats for air temp: " + str(minListByMonth_air_temp))
    df_list = pd.DataFrame({'data': minListByMonth_air_temp, 'name': month_lst})
    chart2 = Chart(data=df_list, height=height, width=width).mark_bar(color='lightgreen').encode(
        X('name', axis=Axis(title='Month'), sort= None),
        Y('data', axis=Axis(title='Min'))
    )
    return chart2.to_json()

@app.route('/maxStats/prep')
def serve_max_stats_prep():
    maxListByMonth_prep = proxy.summarizer.getMaxStatsByMonth('PRECIPITATION')
    print("here in max stats (prep): " + str(maxListByMonth_prep))
    df_list = pd.DataFrame({'data': maxListByMonth_prep, 'name': month_lst})
    chart1 = Chart(data=df_list, height=height, width=width).mark_bar(color='blue').encode(
        X('name', axis=Axis(title='Month'), sort=None),
        Y('data', axis=Axis(title='Max'))
    ).properties(
        title='Precipitation'
    )
    return chart1.to_json()


@app.route('/minStats/prep')
def serve_min_stats_prep():
    minListByMonth_prep = proxy.summarizer.getMinStatsByMonth('PRECIPITATION')
    # print("here in min stats (prep): " + str(minListByMonth_prep))
    minListByMonth_prep = [-1 if a == 10000 else a for a in minListByMonth_prep]
    print(minListByMonth_prep)

    df_list = pd.DataFrame({'data': minListByMonth_prep, 'name': month_lst})
    chart2 = Chart(data=df_list, height=height, width=width).mark_bar(color='lightgreen').encode(
        X('name', axis=Axis(title='Month'), sort= None),
        Y('data', axis=Axis(title='Min'))
    ).properties(
        title='Precipitation'
    )
    return chart2.to_json()

if __name__ == '__main__':
    app.run()