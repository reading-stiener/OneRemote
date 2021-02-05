import json

remote1 = {
    'name': 'Roku',
    'beacon': 432,
    'buttons': [{'img': 'power.png', 'loc': [5, 5], 'size': [25, 25], 'tap': 'g3gr3w'},
                {'img': 'home.png', 'loc': [170, 5], 'size': [25, 25], 'tap': 'g3gr3w'}],
    'trackpads': [{'loc': [5, 35], 'size': [190, 190], 'left': 'f43f43f', 'right': '4g3f43f', 'up': 'sdfsdsd', 'down': '3h8dfj92', 'tap': 'j2f34'}],
    'sliders': [{'loc': [5, 230], 'size': [190, 120], 'left': 'f43f43f', 'right': '4g3f43f', 'tap': 'j2f34', 'labels': ['MENU', 'GUIDE', 'INFO']},
                {'loc': [5, 355], 'size': [190, 120], 'left': 'f43f43f', 'right': '4g3f43f', 'tap': 'j2f34', 'labels': ['DOWN', 'VOL', 'UP']}]
}

remote2 = {
    'name': 'Lights',
    'beacon': 222,
    'buttons': [{'img': 'power.png', 'loc': [5, 5], 'size': [25, 25], 'tap': 'g3gr3w'},
                {'img': 'home.png', 'loc': [170, 5], 'size': [25, 25], 'tap': 'g3gr3w'},
                {'img': 'power.png', 'loc': [10, 360], 'size': [25, 25], 'tap': 'g3gr3w'},
                {'img': 'home.png', 'loc': [165, 360], 'size': [25, 25], 'tap': 'g3gr3w'}],
    'trackpads': [{'loc': [5, 35], 'size': [190, 190], 'left': 'f43f43f', 'right': '4g3f43f', 'up': 'sdfsdsd', 'down': '3h8dfj92', 'tap': 'j2f34'}],
    'sliders': [{'loc': [5, 230], 'size': [190, 120], 'left': 'f43f43f', 'right': '4g3f43f', 'tap': 'j2f34', 'labels': ['DOWN', 'B', 'UP']}]
}

with open("./remotes/%s.json" % remote1['name'], "w+") as write_file:
    json.dump(remote1, write_file)

with open("./remotes/%s.json" % remote2['name'], "w+") as write_file:
    json.dump(remote2, write_file)