class Building:
    def __init__(self):
        self.storage = []


class Warehouse(Building):
    def __init__(self, time_to_reach):
        Building.__init__(self)
        self.time_to_reach = time_to_reach

    def check_delivery(self, number_of_containers):
        return len(self.storage) == number_of_containers

    def receive_the_parcel(self, container):
        self.storage.append(container)
        print('Unloading')


class Transport:
    def __init__(self):
        self.destination = None
        self.time_left = 0  # time left to a specific destination
        self.is_at_home = True
        self.payload = None

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
            self.destination.receive_the_parcel(self.payload)
        if self.time_left == 0:
            self.is_at_home = True
            print('Again at home')


class Factory(Building):
    def __init__(self, containers, trucks: list, warehouses):
        Building.__init__(self)
        self.storage = list(containers)
        self.trucks = trucks
        self.warehouses = warehouses

    def delivery(self):
        for truck in self.trucks:
            if truck.is_at_home:
                if self.storage:
                    container = self.storage.pop(0)
                    truck.move(self.warehouses[container], container)
                    print(f'Moving {container}')
                else:
                    print('No containers')
            else:
                print('This transport is not available')


class Port(Factory, Warehouse):
    def __init__(self, containers, trucks: list, warehouses, time_to_reach):
        Factory.__init__(self, containers, trucks, warehouses)
        Warehouse.__init__(self, time_to_reach)


if __name__ == '__main__':
    containers = input()
    assert len(containers) == containers.count('A') + containers.count('B'), 'Incorrect destination'
    ship = Transport()
    truck_1 = Transport()
    truck_2 = Transport()
    warehouse_A = Warehouse(4)
    warehouse_B = Warehouse(5)
    port = Port([], [ship], {'A': warehouse_A}, 1)
    factory = Factory(containers, [truck_1, truck_2], {'A': port, 'B': warehouse_B})
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
