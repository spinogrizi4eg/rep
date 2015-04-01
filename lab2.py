from spyre import server
import pandas as pd
from datetime import datetime
d = datetime.now()

class StockExample(server.App):
    title = "Lab2 Dushkevych"

    inputs = [
            { "input_type": 'dropdown',
            "label": 'what to show',
            "options": [{"label": "VCI", "value": "VCI"},
                        {"label": "TCI", "value": "TCI"},
                        {"label": "VHI", "value": "VHI"}],
            "variable_name": 'column',
            "action_id": "update_data" },
            {"input_type": 'dropdown',
            "label": 'Oblast`',
            "options": [{"label": "Vinnycia", "value": "1"},
                        {"label": "Volinska", "value": "2"},
                        {"label": "Dnipropetrovska", "value": "3"},
                        {"label": "Donecka", "value": "4"},
                        {"label": "Zhitomirska", "value": "5"},
                        {"label": "Zakarpatska", "value": "6"},
                        {"label": "Zaporizka", "value": "7"},
                        {"label": "Ivano-Frankovska", "value": "8"},
                        {"label": "Kyivska", "value": "9"},
                        {"label": "Kirovogradska", "value": "10"},
                        {"label": "Luganska", "value": "11"},
                        {"label": "Lvivska", "value": "12"},
                        {"label": "Mykolaivska", "value": "13"},
                        {"label": "Odeska", "value": "14"},
                        {"label": "Poltavska", "value": "15"},
                        {"label": "Rivnenska", "value": "16"},
                        {"label": "Sumska", "value": "17"},
                        {"label": "Ternopilska", "value": "18"},
                        {"label": "Kharkivska", "value": "19"},
                        {"label": "Khersonska", "value": "20"},
                        {"label": "Khmelnicka", "value": "21"},
                        {"label": "Cherkaska", "value": "22"},
                        {"label": "Chernivetska", "value": "23"},
                        {"label": "Chernigivska", "value": "24"},
                        {"label": "Crimea", "value": "25"},
                        {"label": "Kyiv", "value": "26"},
                        {"label": "Sevastopol'", "value": "27"},],
            "variable_name": 'province',
            "action_id": "update_data"},

            { "input_type": 'text',
            "label": 'Year',
            "value": '2007',
            "variable_name": 'year',
            "action_id": "update_data" },

            { "input_type": 'text',
            "label": 'Week \n From',
            "value": '10',
            "variable_name": 'week_start',
            "action_id": "update_data" },

            { "input_type": 'text',
            "label": 'To',
            "value": '20',
            "variable_name": 'week_end',
            "action_id": "update_data" }]

    controls = [
                { "control_type": "hidden",
                "label": "get historical value of VCI/TCI/VHI",
                "control_id": "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [
                { "output_type": "plot",
                "output_id": "plot",
                "control_id": "update_data",
                "tab": "Plot",
                "on_page_load": True },

                { "output_type": "table",
                "output_id": "table_id",
                "control_id": "update_data",
                "tab": "Table",
                "on_page_load": True }]

    def getData(self, params):
        column = params['column']
        province = params['province']

        try:
            year = int(params['year'])
        except ValueError:
            year = 2000

        try:
            week_start = int(params['week_start'])
        except ValueError:
            week_start = 1

        try:
            week_end = int(params['week_end'])
        except ValueError:
            week_end = 52

        if week_start < 1 or week_start > week_end or week_start > 52:
            week_start = 1

        if week_end > 52 or week_end < 1:
            week_end = 52

        if year > 2015 and week_end > 5 or year < 1982:
            year = 2000

        df = pd.read_csv('vhi_id_' + str(province) + '_' + str(d.date()) + '.csv', index_col=False, header=1)
        df = df[df['year'] == int(year)]
        df = df[df['week'] >= int(week_start)]
        df = df[df['week'] <= int(week_end)]
        df = df[['week', column]]
        return df
    def getPlot(self, params):
        df = self.getData(params)
        plt_obj = df.set_index('week').plot()
        plt_obj.set_ylabel(list(df[:0])[1])
        plt_obj.set_title('Table')
        fig = plt_obj.get_figure()
        return fig
app = StockExample()
app.launch(port=8080)
