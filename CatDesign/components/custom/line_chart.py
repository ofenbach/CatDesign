from CatDesign.components.layout.box import box

def line_chart(ui, color_scheme, data=None, labels=None, css='', tailwind=''):
    """
    :param data: List of series for the chart. Each series should be a list of data points.
    :param labels: Labels for the x-axis of the chart.
    """
    # Default values if none provided
    if data is None:
        data = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55]]
    if labels is None:
        labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5']

    # Assigning a color scheme for the chart to match the CatDesign style
    color_chart_scheme = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    # Creating the chart options
    chart_options = {
        'chart': {'type': 'line', 'backgroundColor': 'transparent'},
        'title': False,
        'xAxis': {'categories': labels, 'labels': {'style': {'color': '#fff'}}},
        'yAxis': {
            'title': False,
            'gridLineWidth': 0,  # This removes the grid lines
            'labels': {'style': {'color': '#fff'}}
        },
        'legend': {'itemStyle': {'color': '#fff'}},
        'plotOptions': {
            'series': {
                'marker': {
                    'enabled': True,
                    'radius': 5  # Adjust to change marker size
                },
                'lineColor': '#606063',
                'lineWidth': 2,
                'fillOpacity': 0.3  # Transparency of the filled area under the line
            }
        },
        'series': [{'name': f'Series {i+1}', 'data': datum, 'color': color_chart_scheme[i]} for i, datum in enumerate(data)]
    }

    with box(ui, color_scheme=color_scheme, css=f'height: 400px; width: 100%;' + css, tailwind=tailwind):
        ui.chart(chart_options)
