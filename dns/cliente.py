from dns.resolver import Resolver

res = Resolver(configure=False)
res.nameservers = ['127.0.0.1']
res.port = 1053

# SOA
r = res.query('ederson.torresini', 'SOA')
for item in r:
    print('SOA (domínio):')
    print(item, '\n')

# NS
r = res.query('ederson.torresini', 'NS')
for item in r:
    print('NS (domínio):')
    print(item, '\n')

# A
r = res.query('ederson.torresini', 'A')
for item in r:
    print('A (domínio):')
    print(item, '\n')


# A: www
r = res.query('www.ederson.torresini', 'A')
for item in r:
    print('A (www):')
    print(item)
