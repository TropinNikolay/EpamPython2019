class Building:
    def __init__(self, name, **kwargs):
        self.storage = []
        self.name = name


class Warehouse(Building):
    def __init__(self, *, name, time_to_reach, **kwargs):
        super().__init__(name=name, **kwargs)
        self.time_to_reach = time_to_reach

    def check_delivery(self, number_of_containers):
        return len(self.storage) == number_of_containers

    def receive_the_parcel(self, name, container):
        self.storage.append(container)
        print(f'{name} is unloading ...')


class Transport:
    def __init__(self, name):
        self.destination = None
        self.time_left = 0  # time left to a specific destination
        self.is_at_home = True
        self.payload = None
        self.name = name

    def move(self, destination: Warehouse, payload):
        self.destination = destination
        self.time_left = 2 * destination.time_to_reach
        self.is_at_home = False
        self.payload = payload

    def step(self):
        if self.is_at_home:
            return
        self.time_left -= 1
        if self.time_left == self.destination.time_to_reach:
            self.destination.receive_the_parcel(self.name, self.payload)
        if self.time_left == 0:
            self.is_at_home = True
            print(f'{self.name} again at home')


class Factory(Building):
    def __init__(self, *, name, containers, transport: list, warehouses, **kwargs):
        super().__init__(name=name, **kwargs)
        self.storage = list(containers)
        self.transport = transport
        self.warehouses = warehouses

    def delivery(self):
        for transport in self.transport:
            if transport.is_at_home:
                if self.storage:
                    container = self.storage.pop(0)
                    transport.move(self.warehouses[container], container)
                    print(f'{transport.name} departed from {self.name} with cargo {container}')
                else:
                    print(f'No cargo on {self.name}')
            else:
                print(f'{transport.name} is not available on {self.name}')


class Port(Factory, Warehouse):
    def __init__(self, *, name, containers, transport: list, warehouses, time_to_reach):
        super().__init__(name=name, containers=containers, transport=transport, warehouses=warehouses,
                         time_to_reach=time_to_reach)


if __name__ == '__main__':
    containers = input()
    assert len(containers) == containers.count('A') + containers.count('B'), 'Incorrect destination'
    ship = Transport('Princess yacht')
    truck_1 = Transport('Ferrari')
    truck_2 = Transport('Lamborghini')
    warehouse_A = Warehouse(name='A', time_to_reach=4)
    warehouse_B = Warehouse(name='B', time_to_reach=5)
    port = Port(name='PORT', containers=[], transport=[ship], warehouses={'A': warehouse_A}, time_to_reach=1)
    factory = Factory(name='FACTORY', containers=containers, transport=[truck_1, truck_2],
                      warehouses={'A': port, 'B': warehouse_B})
    time = 1
    while True:
        print('======================================================')
        print(f'Start of Day {time}')
        factory.delivery()
        port.delivery()
        truck_1.step()
        truck_2.step()
        ship.step()
        if warehouse_A.check_delivery(containers.count('A')) and warehouse_B.check_delivery(containers.count('B')):
            break
        time += 1
    print()
    print(time)
