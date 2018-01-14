from sodapy import Socrata


class SodaConnector:

    def __init__(self, domain):
        username = "weber.johanes@gmail.com"
        password = "test#123"
        appToken = "vWSR699ElPnWWrJDH90VsNXij"
        self.client = Socrata(domain, appToken , username=username, password=password)

    def get_data(self, dataset_identifier, limit):
        ''' Examples:
        https://soda.demo.socrata.com/resource/4tka-6guv.json?$where=magnitude > 3.0
        client.get("nimj-3ivp", where="depth > 300", order="magnitude DESC", exclude_system_fields=False)
        client.get("nimj-3ivp", region="Kansas")
        '''
        data = self.client.get(dataset_identifier, content_type="json", limit=limit)
        return data