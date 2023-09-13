import requests


url = 'https://script.googleusercontent.com/macros/echo?user_content_key=NenZD9gakocbiOoGhH6OzCxZOBJJLDlGT4G3HQELaPzXjICPomz9dl25yBgvj6g3CeBVR0WxFyz_uNb9RZEf95arHsDy0nHym5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnLKny_gE5DMIdjlvbrWv9xoxuwxDqOpqCJs3UglsWjoAQ2lWu5fxfSVJyUVZburi0qSx8k1m6RR7rBLdTtHOSjM1uAHAYJN0Sdz9Jw9Md8uu&lib=MIzSw3Mi5stBFbGvsTZ7v23Ppx8Xgm0M2'

check_url = requests.get(url)

checking_url = check_url.json()


money_remainder = sum([product['money'] * product['remainder'] for product in checking_url['magazine']])
print(money_remainder)

money_remainder_not_gluten = sum([product['money'] * product['remainder'] for product in checking_url['magazine'] if not['gluten']])
print(money_remainder_not_gluten)
