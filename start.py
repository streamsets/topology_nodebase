from clusterdock.models import Cluster, Node, NodeGroup


def main(args):
    image = '{}/topology_nodebase:{}'.format('/'.join(args.registry, args.namespace)
                                             if args.registry
                                             else args.namespace,
                                             args.operating_system)

    cluster = Cluster(NodeGroup(name='nodes',
                                nodes=[Node(hostname=hostname, image=image)
                                       for hostname in args.nodes]))
    cluster.start(args.network)
