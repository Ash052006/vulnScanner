import PortScanner

targets_ip=input('[+] * Enter Target To Scan For Vulnerable Open Ports:  ')
Port_number=int(input('[+] * Enter Amount of Ports You Want To Scan(500- First 500 ports): '))
vul_file=input('[+] * Enter Vulnerable File Path: ')
print('\n')

PortScanner.scan(targets_ip)