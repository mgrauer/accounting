
class Accounts():

    def __init__(self):
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def balances(self):
        print('Balances')
        for account in self.accounts:
            account.status()
   
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

def txn(debitAccounts, creditAccounts, amount=None):
    if amount is not None:
        # shorthand for a simple transaction
        debitAccounts = [(debitAccounts, amount)]
        creditAccounts = [(creditAccounts, amount)]
    totalDebits = sum([a for d,a in debitAccounts])
    totalCredits = sum([a for d,a in creditAccounts])
    if totalDebits != totalCredits:
        raise Exception("Total credits != total debits")
    print('TXN')
    for d,a in debitAccounts:
        d.debit(a)
        print(('Dr. %s %d') % (d.shortName, a))
    for c,a in creditAccounts:
        c.credit(a)
        print(('\tCr. %s %d') % (c.shortName, a))




debits = [('cash', 'cash'),
          ('inventory', 'i'),
          ('accounts receivable', 'ar'),
          ('notes receivable', 'nr')]
credits = [('accounts payable', 'ap'),
          ('common stock', 'cs'),
          ('additional paid in capital', 'apic'),
          ('notes payable', 'np')]

drs = {}
for name, shortName in debits:
    debit = Debit(name, shortName)
    drs[name] = debit
    drs[shortName] = debit

crs = {}
for name, shortName in credits:
    credit = Credit(name, shortName)
    crs[name] = credit
    crs[shortName] = credit

txn(drs['cash'], crs['np'], 100)
txn(crs['np'], drs['cash'], 20)
txn(drs['i'], drs['cash'], 10)
txn(crs['np'], crs['cs'], 80)
txn([(drs['cash'], 150000)], [(crs['cs'], 50000), (crs['apic'], 100000)])
accounts.balances()
