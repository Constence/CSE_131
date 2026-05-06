
import json 

def write_data_to_json_file(data, filename):
    '''Write the data contained in the data to the file whose name is filename. Make sure to check and catch errors '''
    try:
        with open (filename, 'wt') as filehandle:
            #json_data = json.dumps(data)
            #filehandle.write(json_data)
            json.dump(data, filehandle)
    except (FileExistsError, FileNotFoundError): 
        print("file not found")

def read_json_data(filename):
    '''Read the data from the filename and return the json formatted data'''
    try:
        with open (filename, 'rt') as filehandle:
            json_data = filehandle.read()
            dictonary_data = json.loads(json_data)
    except (FileExistsError, FileNotFoundError): 
        print("file not found")

    return dictonary_data

def pay_me_back(filename):
    """Print out the my_friends and only show what is owed"""
    try:
        with open (filename, 'rt') as filehandle:
            json_data = filehandle.read()
            dictonary_data = json.loads(json_data)
    except (FileExistsError, FileNotFoundError): 
        print("file not found")

    return dictonary_data(['Owe me'])

    


def main():
    #print('Hey')
    my_friends = {
        "Names": ['Bob', 'betty', 'jeannie'], 
        "Phone Numbers": [1234567890, 2086541234, 2088673598], 
        "Address": ['555 cherry lane', '456 huntsdale ct', '934 temple lane'], 
        "Owe me": [123.45, 456.12, -34.20]
     }
    
    filename = 'myfriends.json'
    write_data_to_json_file(my_friends, filename)
    my_friends_data = read_json_data(filename)
    #print(my_friends_data['Names'])
    print(pay_me_back(my_friends))
    

main() 