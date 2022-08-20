import person_pb2

if __name__ == '__main__':
    per = person_pb2.Person()
    per.name = 'Tom'
    per.age = 20
    encoded_bytes = per.SerializeToString()
    print('encoded types: ', encoded_bytes)

    new_per = person_pb2.Person()
    new_per.ParseFromString(encoded_bytes)
    print(new_per)
    
