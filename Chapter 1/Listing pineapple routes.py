portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    if len(route) == 5:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in ports:
            new_port_list = ports.copy()
            new_route_list = route.copy()
            new_route_list.append(i)                                                                                                                                                                                                                                                                                                                                                                                                                            
            new_port_list.remove(i)
            permutations(new_route_list, new_port_list)

permutations([0], list(range(1, len(portnames))))