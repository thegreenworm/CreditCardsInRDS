import psycopg2
from scripts import Creating
from model.datamodels import DbClient
import sys
import getopt

upload = Creating()
clientArgument = DbClient()

usage = """
usage:
 program -g or -balanceGreaterThan : amount
 program -l or -balanceLessThan : amount
 program -o or -overdrawn
 program -e or -expired
# """
clientList = []
# command = sys.argv[1]

try:
    opts, args = getopt.getopt(sys.argv[1:],'g:l:oe',['balanceGreaterThan=','balanceLessThan=','overdrawn','expired'])
except getopt.GetoptError:
    print(usage)
    sys.exit()

clientList.clear()
for opt in opts:
    if '-g' in opt[0]:
        if opt[1] == '-e' or opt[1] == '-l' or opt[1] == '-o' or opt[1] == None:
            clientList = clientList
        elif len(clientList) == 0:
            clientList = clientArgument.balanceGreaterThan(opt[1])
        else:
            clientList = clientArgument.balanceGreaterThanList(opt[1],clientList)
    elif '-l' in opt[0]:
        if opt[1] == '-e' or opt[1] == '-g' or opt[1] == '-o' or opt[1] == None:
            clientList = clientList
        elif len(clientList) == 0:
            clientList = clientArgument.balanceLessThan(opt[1])
        else:
            clientList = clientArgument.balanceLessThanList(opt[1],clientList)
    elif '-' in opt[0]:
        if opt[1] == '-e' or opt[1] == '-l' or opt[1] == '-g':
            clientList = clientList
        elif len(clientList) == 0:
            clientList = clientArgument.overdrawn()
        else:
            clientList = clientArgument.overdrawnList(clientList)
    elif '-e' in opt[0]:
        if opt[1] == '-g' or opt[1] == '-l' or opt[1] == '-o':
            clientList = clientList
        elif len(clientList) == 0:
            clientList = clientArgument.expired()
        else:
            clientList = clientArgument.expiredList(clientList)
    
if len(clientList) == 0:
    print("\nNo matching results found\n")
else:
    for client in clientList:
        print(f"""
            id: {client[0]}
            first name: {client[1]}
            last name: {client[2]}
            card number: {client[3]}
            expiration date: {client[4]}
            balance: {client[5]}
            --------------------------------------
        """)





# upload.createTableClients()
# upload.uploadJSON()

