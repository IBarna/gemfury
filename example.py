import json
import random

class Some(object):

    def get_events(self):
        """Load json file with events and update events field."""
        # event_id = int(time.time() * 1000)
        # event_id = random.randint(1, 999999999)
        event_id = 15023937
        with open('./event_details.json') as events_file:
            self.data = json.load(events_file)
        self.data['id'] = event_id
        self.data['matchId'] = event_id
        self.data['rbid'] = event_id

        print self.data['id']

    def openbetid_mapping(self):
        """Providing openBetID mapping and sending openBetID for Server.
        :return: None
        """
        # Configuring data for send post mapping reques
        # t
        openBetID = random.randint(1, 9999999)

        self.data_mapping = {
            "openbetId": openBetID,
            "id": self.data['id'],
            "type": "auto"
        }
        print self.data_mapping

    def load_incidents(self):
        """Load json file with incidents and update incident fields."""
        events = self.data
        print events['uuid']
        with open('./incident_events.json') as incident_file:
            self.data_incident = json.load(incident_file)
        for self.incident in self.data_incident['incidents']:
            self.incident['eventId'] = events['id']
            print 'This is type...', type(self.incident)
            # for field in incident['payload']:
            #     incident['payload']['eventId'] = events['id']
            #     incident['payload']['ID'] = events['id']




a = Some()
a.get_events()
a.openbetid_mapping()
a.load_incidents()



data_mapping = {
            "openbetId": 2222222,
            "id": 111111,
            "type": "auto"
        }
print data_mapping['openbetId']

body_mapping = json.dumps(data_mapping)
