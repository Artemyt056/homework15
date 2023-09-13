import requests


url = 'https://script.googleusercontent.com/macros/echo?user_content_key=NenZD9gakocbiOoGhH6OzCxZOBJJLDlGT4G3HQELaPzXjICPomz9dl25yBgvj6g3CeBVR0WxFyz_uNb9RZEf95arHsDy0nHym5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnLKny_gE5DMIdjlvbrWv9xoxuwxDqOpqCJs3UglsWjoAQ2lWu5fxfSVJyUVZburi0qSx8k1m6RR7rBLdTtHOSjM1uAHAYJN0Sdz9Jw9Md8uu&lib=MIzSw3Mi5stBFbGvsTZ7v23Ppx8Xgm0M2'

check_url = requests.get(url)

checking_url = check_url.json()

money = sum([person['money'] for person in checking_url['magazine']])
money_remainder = sum([product['remainder'] for product in checking_url['magazine']])
money_and_remainder = money * money_remainder
print(money_and_remainder)

money_not_gluten_ = sum([person['money'] for person in checking_url['magazine'] if not['gluten']])
money_not_gluten_remainder = sum([product['remainder'] for product in checking_url['magazine']])
money_not_gluten_and_remainder = money_not_gluten_ * money_not_gluten_remainder
print(money_not_gluten_and_remainder)
