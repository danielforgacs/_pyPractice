test_data = zip(list('abcdefgh'), list('qwertypo'))
test_data = (
    'Lorem ipsum dolor sit amet consectetur adipiscing'
    ' elit Maecenas id massa id velit maximus bibendum'
    # ' Nunc eu sem ut justo pellentesque volutpat sit'
    # ' amet eget mi Donec turpis dui mattis ac vestibulum'
    # ' eu malesuada id tellus Quisque non lacinia justo'
    # ' et scelerisque nisi Cras semper erat non tincidunt varius'
    )
db = test_data.split()


def get_data():
    for element in db:
        yield element, str(len(element))
