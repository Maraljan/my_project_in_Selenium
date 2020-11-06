

def join_coma(*args, **kwargs):
    print(args)
    print(kwargs)
    return ','.join(map(str, args)) + ',' + ','.join(f'{key}:{value}' for key, value in kwargs.items())


# print(join_coma(1, 3, 4, 5, 'maral', doma='lol', educa='ppoopo'))



database = {
    'vova': '1',
    'maral': '1',
    'mahru': '2',
    'bater': '2',
}


def get_from_database(where, default=None):

    default = default or []

    people = []
    for name, value in database.items():
        if value == where:
            people.append(name)
    if people:
        return people
    return default


print(get_from_database('2', 'Not found'))
print(get_from_database('1', 'Not found'))

result = get_from_database('0')

result.append('my_person')

print(result)

new_result = get_from_database('0')
print(new_result)