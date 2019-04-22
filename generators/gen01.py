def g():
    while True:
        item = yield
        print('recieved:', item)

        if item == 'exit':
            break

        yield item