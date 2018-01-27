from sodapy import Socrata


class SodaConnector:

    def __init__(self, domain):
        username = "weber.johanes@gmail.com"
        password = "test#123"
        app_token = "vWSR699ElPnWWrJDH90VsNXij"
        self.client = Socrata(domain, app_token , username=username, password=password)

    def get_data(self, dataset_identifier, from_date, to_date):
        ''' Examples:
        https://soda.demo.socrata.com/resource/4tka-6guv.json?$where=magnitude > 3.0
        client.get("nimj-3ivp", where="depth > 300", order="magnitude DESC", exclude_system_fields=False)
        client.get("nimj-3ivp", region="Kansas")
        '''
        where_statement = "created_date >='" + str(from_date) + "' AND created_date <'" + str(to_date) + "'"
        data = self.client.get(dataset_identifier,
                               content_type="json",
                               where=where_statement,
                               order="created_date DESC",
                               limit=100000)
        return data