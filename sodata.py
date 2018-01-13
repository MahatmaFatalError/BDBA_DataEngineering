from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", "vWSR699ElPnWWrJDH90VsNXij", username="weber.johanes@gmail.com", password="test#123")
metadata = client.get("fhrw-4uyv", content_type="json", limit=2)
print(metadata)