import requests


url = 'https://script.googleusercontent.com/macros/echo?user_content_key=tl4jsL9vzu2dCxH7nFqvkCaA0fjdGnVpJnp0suJvN73Z1CQPc5bvjEH7lgPS5dNkA_UU6pEDyNEqIVP-vH1DSXKxx1CVpvk7m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnObB0kwUlVQh5Mo_4h0OkP9qmMhZMYpNiEqs0LzczH870hC4DVlpCU8BRi8qLLDAttZJlRufWV8M_OsAq0ThyCyqbM5bgh1mlNz9Jw9Md8uu&lib=MIzSw3Mi5stBFbGvsTZ7v23Ppx8Xgm0M2'

check_url = requests.get(url)

checking_url = check_url.json()

money = sum([person['money'] for person in checking_url['trip'] if not['gluten']])
print(money)
