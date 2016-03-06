# -*- coding: utf-8 -*-
import pygal

world_map_chart = pygal.Worldmap()
world_map_chart.title = 'United States Allies and China'
world_map_chart.add('China', ['cn'])
world_map_chart.add('U.S. Allies', ['al',
                                   'be', 'bg', 'ca', 'hr', 'cz', 'dk', 'ee', 'ff', 'de', 'hu', 'is', 'it',
                                   'lv', 'lt', 'lu', 'nl', 'no', 'pl', 'pt', 'ro', 'si', 'sk', 'tr', 'us', 'uk'])

# Render file.
world_map_chart.render_to_file('world_map.svg')
