import time
import json
import random

import requests

tournament_dict = {
  "identifier": "4nidzmunvpvxk1ir9b6m8mpay",
  "tournamentName": "Ukrainian Football League",
  "location": "Ukraine",
  "stadium": "Dynamo",
  "league": "Ukrainian Football",
  "startDate": "2016-07-11 19:00:00 GMT-0000",
  "sportName": "football",
  "providerName": "perform"
}


def update_tournament():
    """Update fields in tournament dictionary.
    :return:dict
    """
    tournament_dict['identifier'] = 'r56f0430409b488e99880c4e1fd22cd5'
    tournament_dict['startDate'] = time.strftime("%Y-%m-%d %H:%M:%S GMT-0000")
    return tournament_dict


def load_events():
    """Load json file with events and update events field.
    :return:dict
    """
    tournament = update_tournament()
    # event_id = int(time.time() * 1000)
    event_id = 1502303120430
    with open('./event_details.json') as events_file:
        data = json.load(events_file)
    data['id'] = event_id
    data['matchId'] = event_id
    data['rbid'] = event_id
    data['homeTeam'] = 'Dnipro'
    data['homeTeamAbbr'] = 'DNP'
    data['awayTeam'] = 'Shachtar'
    data['awayTeamAbbr'] = 'SHC'
    data['name'] = data['homeTeam'] + ' vs ' + data['awayTeam']
    data['tournamentID'] = tournament['identifier']
    data['leagueUuid'] = tournament['identifier']
    data['stadium'] = tournament['stadium']
    data['league'] = tournament['league']
    data['country'] = 'Ukraine'
    data['uuid'] = '4poiu4cdfh0v0679mndd9vyb6'
    data['date'] = time.strftime("%Y-%m-%d %H:%M:%S")
    data['startTime'] = time.strftime("%Y-%m-%d %H:%M:%S")
    data['startDate'] = time.strftime("%a %b %d %Y %H:%M:%S GMT+0000 (UTC)")
    return data


def load_incidents():
    """Load json file with incidents and update incident fields.
    :return:dict
    """
    events = load_events()
    with open('./incident_events.json') as incident_file:
        data_incident = json.load(incident_file)
    for incident in data_incident['incidents']:
        incident['eventId'] = events['id']
        for field in incident['payload']:
            incident['payload']['eventId'] = events['id']
            incident['payload']['ID'] = events['id']
            incident['payload']['UUID'] = events['uuid']
    return data_incident['incidents']


data_tournament = update_tournament()
data_events = load_events()
body_tournament = json.dumps(data_tournament, indent=2)
body_events = json.dumps(data_events, indent=2)
vis_rtc_url = 'https://vis-tst2-coral.symphony-solutions.eu'
sport = 'football'
provider = 'perform'
content_type_headers = {"Content-Type": "application/json"}
post_tournament = requests.post(url=vis_rtc_url + '/storeTournament/%s/%s' % (sport, provider),
                                headers=content_type_headers, data=body_tournament, verify=False)
post_events = requests.post(url=vis_rtc_url + '/matchDetails/%s/%s' % (sport, provider),
                            headers=content_type_headers, data=body_events, verify=False)

openBetID = random.randint(1, 9999999)
data_mapping = {
    "openbetId": openBetID,
    "id": data_events['id'],
    "type": 'auto'
}
body_mapping = json.dumps(data_mapping)
post_mapping = requests.post(url=vis_rtc_url + '/addMapping/%s/%s' % (sport, provider),
                             headers=content_type_headers, data=body_mapping, verify=False)

data_incident = load_incidents()
# for incident in data_incident['incidents']:
for incident in data_incident[:]:
    body_incident = json.dumps(incident['payload'], indent=2)
    # print body_incident
    post_incident = requests.post(url=vis_rtc_url + '/storeIncident/%s/%s' % (sport, provider),
                                  headers=content_type_headers, data=body_incident, verify=False)

print '*** Post incidents details: Response code is %s, content %s' % (post_incident.status_code, post_incident.content)

print '*** Post tournament details: Response code is %s, content %s' % (post_tournament.status_code, post_tournament.content)

print '*** Post event details: Response code is %s, content %s' % (post_events.status_code, post_events.content)

print '*** Post mapping details: Response code is %s, content %s' % (post_mapping.status_code, post_mapping.content)
