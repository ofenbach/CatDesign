from CatDesign.components.layout.box import box

def line_chart(ui, color_scheme, data=None, labels=None, css='', tailwind=''):
    """
    :param data: List of series for the chart. Each series should be a list of data points.
    :param labels: Labels for the x-axis of the chart.
    """
    # Default values if none provided
    if data is None:
        data = [[15, 25, 10, 32, 40, 60, 30, 15, 20,25, 28,26,20]]
    if labels is None:
        labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5']

    # Assigning a color scheme for the chart to match the CatDesign style
    color_chart_scheme = ['#6CCAFF']  # CatDesign blue

    # Creating the chart options
    chart_options = {
        'chart': {'type': 'areaspline', 'backgroundColor': 'transparent'},
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
                    'enabled': False,
                    'radius': 1  # Adjust to change marker size
                },
                'line': {
                    'dashStyle': 'Solid'
                },
                'fillColor': {
                    'linearGradient': { 'x1': 0, 'y1': 0, 'x2': 0, 'y2': 1 },
                    'stops': [
                        [0, '#6CCAFF'],  # Gradient starts with CatDesign blue
                        [1, 'rgba(0,0,0,0)']  # Gradient to transparent
                    ]
                },
                'fillOpacity': 0.5  # Transparency of the filled area
            }
        },
        'series': [{'name': f'Series {i+1}', 'data': datum, 'color': color_chart_scheme[0]} for i, datum in enumerate(data)]
    }

    with box(ui, color_scheme=color_scheme, css=f'' + css, tailwind=tailwind):
        ui.chart(chart_options)
