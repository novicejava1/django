﻿Imports FusionCharts.Charts
Partial Class Pages_CommonThemeUsage
    Inherits System.Web.UI.Page
    Protected Sub Page_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        'store chart config data as json string
        Dim firstChartData, secondChartData As String
        firstChartData = "{                      'chart': {                    'caption': 'Split of Sales by Product Category',                    'subCaption': '5 top performing stores  - last month',                    'plotToolText': '<div><b>\\$label</b><br/>Product : <b>\\$seriesname</b><br/>Sales : <b>\\$\\$value</b></div>',                    'theme': 'fusion'                    },                    'categories': [{                      'category': [{                        'label': 'Garden Groove harbour'                      }, {                        'label': 'Bakersfield Central'                      }, {                        'label': 'Los Angeles Topanga'                      }, {                        'label': 'Compton-Rancho Dom'                      }, {                        'label': 'Daly City Serramonte'                      }]                    }],                    'dataset': [{                      'seriesname': 'Non-Food Products',                      'data': [{                        'value': '28800'                      }, {                        'value': '25400'                      }, {                        'value': '21800'                      }, {                        'value': '19500'                      }, {                        'value': '11500'                      }]                    }, {                      'seriesname': 'Food Products',                      'data': [{                        'value': '17000'                      }, {                        'value': '19500'                      }, {                        'value': '12500'                      }, {                        'value': '14500'                      }, {                        'value': '17500'                      }]                    }]                }"
        secondChartData = "{                    'chart': {                    'caption': 'Harry\'s SuperMart',                  'subCaption': 'Top 5 stores in last month by revenue',                  'theme': 'fusion'                  },                  'data':[                    {                        'label': 'Bakersfield Central',                      'value': '880000'                  },                  {                        'label': 'Garden Groove harbour',                      'value': '730000'                  },                  {                        'label': 'Los Angeles Topanga',                      'value': '590000'                  },                  {                        'label': 'Compton-Rancho Dom',                      'value': '520000'                  },                  {                        'label': 'Daly City Serramonte',                      'value': '330000'                  }                  ]              }"
        'create chart instance
        'chart type, chart id, width, height, data format, data source as string
        Dim overlappedColumnChart As New Chart("overlappedcolumn2d", "overlap_chart", "600", "400", "json", firstChartData)
        Dim columnChart As New Chart("column2d", "column_Chart", "600", "400", "json", secondChartData)
        'render chart
        Literal1.Text = overlappedColumnChart.Render()
        Literal2.Text = columnChart.Render()
    End Sub
End Class
