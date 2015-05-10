import json

class Accounts():

    def __init__(self):
        self.accounts = []
        self.names = {}
        self.shortNames = {}

    def addAccount(self, account):
        self.accounts.append(account)
        self.shortNames[account.shortName] = account
        self.shortNames[account.shortName.lower()] = account
        self.names[account.name] = account
        self.names[account.name.lower()] = account

    def balances(self):
        print('Balances')
        for account in self.accounts:
            account.status()
        print('Total debits and credits')
        debs, creds = 0, 0
        for a in self.accounts:
            debs += a.debits
            creds += a.credits
        print('%d\t%d' % (debs, creds))
        if creds != debs:
            raise Exception('Total credits and debits unequal')

    def find(self, name):
        if name in self.shortNames:
            return self.shortNames[name]
        if name in self.names:
            return self.names[name]
        raise Exception('Account %s not found' % name) 




accounts = Accounts()

class Account:

    def __init__(self, name, shortName, accountType):
        self.name = name
        self.shortName = shortName
        self.credits = 0
        self.debits = 0
        self.accountType = accountType
        accounts.addAccount(self)

    def debit(self, amount):
        self.debits += amount

    def credit(self, amount):
        self.credits += amount


class Debit(Account):

    def __init__(self, name, shortName):
        Account.__init__(self, name, shortName, 'debit')

    def status(self):
        print('DR[%s] %d' % (self.shortName, (self.debits - self.credits)))
	print '%s\t%s' % (self.debits, self.credits)

    def increase(self, amount):
        self.debits += amount

    def decrease(self, amount):
        self.credits += amount

class Credit(Account):

    def __init__(self, name, shortName):
        Account.__init__(self, name, shortName, 'credit')

    def status(self):
        print('CR[%s] %d' % (self.shortName, (self.credits - self.debits)))
	print '%s\t%s' % (self.debits, self.credits)

    def increase(self, amount):
        self.credits += amount

    def decrease(self, amount):
        self.debits += amount

def txn(debitAccounts, creditAccounts):#, amount=None):
    totalDebits = sum([a for d,a in debitAccounts])
    totalCredits = sum([a for d,a in creditAccounts])
    if totalDebits != totalCredits:
        raise Exception("Total credits != total debits")
    print('TXN')
    for d,a in debitAccounts:
        d = accounts.find(d)
        d.debit(a)
        print(('Dr. %s %d') % (d.shortName, a))
    for c,a in creditAccounts:
        c = accounts.find(c)
        c.credit(a)
        print(('\tCr. %s %d') % (c.shortName, a))


def createAccountsJson(filepath):
    def getNames(account):
        if 'shortName' not in account:
            shortName = ''.join([word[0:3] for word in account['name'].split()])
        else:
            shortName = account['shortName']
        if shortName in accounts.shortNames:
            raise Exception('shortname %s clash' % shortName)
        return account['name'], shortName

    with open(filepath, 'r') as json_data:
        accountsJson = json.load(json_data)
        for account in accountsJson['debits']:
            name, shortName = getNames(account)
            debit = Debit(name, shortName)
        for account in accountsJson['credits']:
            name, shortName = getNames(account)
            credit = Credit(name, shortName)
