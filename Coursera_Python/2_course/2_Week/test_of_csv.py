# Reading and Writing
import csv

hosts = [['workstation.local', '192.168.1.5'], ['webserver.cloud', '10.4.5.2']]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

#########################################

f = open('csv_file.txt')
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print('Name: {}, Phone: {}, Role: {}'.format(name, phone, role))

#########################################

users = [ {'name': 'Adrian May', 'username': 'mayadri', 'phone': '0412-4458741'}, 
{'name': 'Leon Kennedy', 'username': 'leonk', 'phone': '0412-4568412'}, 
{'name': 'Clair Redfield', 'username': 'clair', 'phone': '0416-4747125'}]

keys = ['name', 'username', 'phone']

with open('by_department', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
