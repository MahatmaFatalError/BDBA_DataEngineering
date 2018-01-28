from sodapy import Socrata


class SodaConnector:

    def __init__(self, domain):
        username = "weber.johanes@gmail.com"
        password = "test#123"
        app_token = "vWSR699ElPnWWrJDH90VsNXij"
        self.client = Socrata(domain, app_token , username=username, password=password)

    def get_data(self, dataset_identifier, **kwargs):
        # arguments can be from_date, to_date and limit
        from_date = None
        to_date = None
        limit = None
        if "from_date" in kwargs:
            from_date = kwargs["from_date"]
        if "to_date" in kwargs:
            to_date = kwargs["to_date"]
        if "limit" in kwargs:
            limit = kwargs["limit"]

        where_statement = "created_date >='" + str(from_date) + "' AND created_date <'" + str(to_date) + "'"
        data = self.client.get(dataset_identifier,
                                   content_type="json",
                                   where=where_statement,
                                   order="created_date DESC",
                                   limit=limit)

        return data