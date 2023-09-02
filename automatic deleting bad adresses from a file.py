''' 
A program that downloads two text files: one with ip addresses
that and the other that contains ip addresses that should not be in the former.
The program converts the files into lists and checks whether any address that
should be removed is in the correct file - if so, it removes it
'''


def update_list(access_list, remove_list):
    #downloading addresses from the first file
    with open(access_list, "r")as file: 
        ip_addresses = file.read()
    
    #downloading addresses from the second file
    with open(remove_list, "r")as file:
        ip_addresses_to_remove = file.read()
    
    #convert strings to lists
    ip_addresses = ip_addresses.split()
    ip_addresses_to_remove = ip_addresses_to_remove.split()
    
    #checking
    for address in ip_addresses_to_remove:
        if address in ip_addresses:
            ip_addresses.remove(address)
        
    #saving a new list to a file
    updated_list = '\n'.join(ip_addresses)
    with open(access_list, "w")as file:
        file.write(updated_list)
        