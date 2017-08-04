from clusterdock.models import Cluster, Node


def main(args):
    image = '{}/{}/topology_nodebase:{}'.format(args.registry,
                                                args.namespace,
                                                args.operating_system)

    cluster = Cluster(*[Node(hostname=hostname, group='nodes', image=image)
                        for hostname in args.nodes])
    cluster.start(args.network)
