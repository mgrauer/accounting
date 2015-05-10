from acc import *

createAccountsJson('relic_accounts.json')


txn([('cash', 250000)], [('comsto', 25000), ('addpai', 225000)])
txn([('LegFeeExp', 3900)], [('cash', 3900)])
txn([('bui', 52000), ('land', 103000)], [('cash', 31000), ('morpay', 124000)])
txn([('bui', 33000)], [('cash', 33000)])
txn([('metdet', 120000)], [('cash', 120000)])
txn([('inv', 2000)], [('accpay', 2000)])
txn([('sof', 2100)], [('cash', 2100)])
txn([('preadv', 8000)], [('cash', 8000)])
txn([('notrec', 5000)], [('cash', 5000)])
txn([('retear', 2500)], [('divpay', 2500)])
txn([('accpay', 2000)], [('cash', 2000)])
txn([('divpay', 2500)], [('cash', 2500)])

accounts.balances()
