'''
Created by NGnius 2019-06-17
'''
from . import misc
import requests

def factory_list(token, body = dict(misc.CRF_BODY)):
    '''(str [, dict]) ->  list of dict
    token: "Token" value in the .auth.fj_login(username, password) dict
    body: search parameters in the format of .misc.CRF_BODY

    returns a list of robots per the request parameters'''

    url = r'https://factory.robocraftgame.com/api/roboShopItems/list'
    headers = misc.make_headers(token)
    response = requests.post(url, json=body, headers=headers)
    return response.json()['response']['roboShopItems']

def factory_bot(token, id):
    '''(str, int) -> dict
    token: "Token" value in the .auth.fj_login(username, password) dict
    id: "itemId" value of an entry in the factory_list(token) list

    returns specific info about the robot referenced by id'''

    url = r'https://factory.robocraftgame.com/api/roboShopItems/get/'+str(id)
    headers = misc.make_headers(token)
    response = requests.get(url, headers=headers)
    return response.json()['response']

def make_search_body(search='', weapon=None, movement=None, maxCpu=2000, minCpu=100, maxRr=100000000, minRr=0, player=None):
    ''' ([...]) -> dict
    params: search parameters, overwrite a param to change it from default
    see .misc.WEAPONS and .misc.MOVEMENTS for valid weapon & movement names (respectively)

    returns the parameters in the API-compatible format'''
    # NOTE: this is not feature complete -- the API supports more stuff than this function
    result = dict(misc.CRF_BODY)  # copy
    result['textFilter'] = search
    if weapon is not None:
        result['weaponCategoryFilter'] = misc.WEAPONS[weapon]
    if movement is not None:
        result['movementCategoryFilter'] = misc.MOVEMENTS[movement]
    result['maximumCpu'] = maxCpu
    result['minimumCpu'] = minCpu
    result['maximumRobotRanking'] = maxRr
    result['minimumRobotRanking'] = minRr
    if player is True:
        result['textSearchField'] = 1
    elif player is False:
        result['textSearchField'] = 2
    else:  # unnecessary but verbose!
        result['textSearchField'] = 0
    return result
