from ad import Client, Creds, activate

domain = 'freeadi.org'
user = 'Administrator'
password = 'Pass123'

creds = Creds(domain)
creds.acquire(user, password)
activate(creds)

client = Client(domain)
users = client.search('(objectClass=user)', scheme='gc')
for dn,attrs in users:
    name = attrs['sAMAccountName'][0]
    domain = client.domain_name_from_dn(dn)
    print '-> %s (%s)' % (name, domain)
