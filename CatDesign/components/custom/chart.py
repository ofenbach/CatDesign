from CatDesign.components.layout.box import box

def bar_chart(ui, color_scheme, data=None, labels=None, css='', tailwind=''):
    """
    :param data: Data for the chart
    :param labels: Labels for the chart
    """
    # Default values if none provided
    if data is None:
        data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    if labels is None:
        labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6', 'Label7', 'Label8', 'Label9', 'Label10']

    # Assigning a color scheme for the chart to match the CatDesign style
    color_chart_scheme = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    # Creating the chart options
    chart_options = {
        'chart': {'type': 'column', 'backgroundColor': 'transparent'},
        'title': False,
        'xAxis': {'categories': labels, 'labels': {'style': {'color': '#fff'}}, 'gridLineWidth': 0},
        'yAxis': {'title': False, 'gridLineColor': '#606063', 'labels': {'style': {'color': '#fff'}}, 'gridLineWidth': 0},
        'legend': {'itemStyle': {'color': '#fff'}},
        'plotOptions': {
            'series': {
                'borderColor': '#000',
                'borderRadius': 8  # New attribute for rounded corners
            }
        },
        'series': [{'name': label, 'data': [datum], 'color': color} for label, datum, color in zip(labels, data, color_chart_scheme)]
    }

    with box(ui, color_scheme=color_scheme, css=f'height: 400px; width: 100%;' + css, tailwind=tailwind):
        ui.chart(chart_options)
