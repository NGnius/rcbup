'''
Created by NGnius 2019-06-17
'''

CRF_BODY = {
		"page": 1,
		"pageSize": 100,
		"order": 0,
		"playerFilter": False,
		"movementFilter": "100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,1200000",
		"movementCategoryFilter": "100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,1200000",
		"weaponFilter": "10000000,20000000,25000000,30000000,40000000,50000000,60000000,65000000,70100000,75000000",
		"weaponCategoryFilter": "10000000,20000000,25000000,30000000,40000000,50000000,60000000,65000000,70100000,75000000",
		"minimumCpu": -1,
		"maximumCpu": -1,
		"minimumRobotRanking": 0,
		"maximumRobotRanking": 1000000000,
		"textFilter": "",
		"textSearchField": 0,
		"buyable": True,
		"prependFeaturedRobot": False,
		"featuredOnly": False,
		"defaultPage": False
	}

# maps user terms to API movement constants
MOVEMENTS = {
    'wheel':100000,
    'hover':200000,
    'wing':300000,
    'thruster':400000,
    'rudder':500000,
    'insect':600000,
    'mech':700000, 'leg':700000,
    'ski':800000,
    'tread':900000, 'tank':900000,
    'rotor':1000000,
    'sprinter':1100000,
    'propeller':1200000, 'prop':1200000
}

# maps user terms to API weapon constants
WEAPONS = {
    'laser':10000000, 'smg':10000000, 'lasor':10000000,
    'plasma':20000000,
    'mortar':25000000,
    'rail':30000000,
    'nano':40000000, 'medic':40000000,
    'tesla':50000000,
    'flak':60000000,
    'ion':65000000,
    'protoseeker':70100000, 'ps':70100000,
    'chain':75000000, 'csh':75000000,
}

# copied from IdeaBot/Robocraft/factory_search.py ttps://github.com/IdeaBot/Robocraft
def make_headers(token):
    headers = dict()
    headers['Authorization'] = "Web "+token
    return headers
