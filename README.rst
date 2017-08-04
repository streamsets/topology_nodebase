=================================
nodebase topology for clusterdock
=================================

This repository houses the **nodebase** topology for `clusterdock`_.

.. _clusterdock: https://github.com/clusterdock/clusterdock

Usage
=====

Assuming you've already installed **clusterdock** (if not, go `read the docs`_),
you use this topology by cloning it to a local folder and then running commands
with the ``clusterdock`` script:

.. _read the docs: http://clusterdock.readthedocs.io/en/latest/

.. code-block:: console

    $ git clone https://github.com/clusterdock/topology_nodebase.git
    $ clusterdock topology_nodebase start
    2017-08-04 09:10:33 AM clusterdock.models   INFO     Starting cluster on network (cluster) ...
    2017-08-04 09:10:33 AM clusterdock.models   INFO     Starting node node-1.cluster ...
    2017-08-04 09:10:33 AM clusterdock.models   INFO     Starting node node-2.cluster ...
    2017-08-04 09:10:34 AM clusterdock.models   INFO     Cluster started successfully (total time: 00:00:01.547).

To see full usage instructions for the ``start`` action, use ``-h``/``--help``:

.. code-block:: console

    $ clusterdock topology_nodebase start -h
    usage: clusterdock start [-h] [--node-disks map] [--always-pull]
                             [--namespace ns] [--network nw] [-o sys] [-r url]
                             [--nodes node [node ...]]
                             topology

    Start a nodebase cluster

    positional arguments:
      topology              A clusterdock topology directory

    optional arguments:
      -h, --help            show this help message and exit
      --always-pull         Pull latest images, even if they're available locally
                            (default: False)
      --namespace ns        Namespace to use when looking for images (default:
                            clusterdock)
      --network nw          Docker network to use (default: cluster)
      -o sys, --operating-system sys
                            Operating system to use for cluster nodes (default:
                            centos6.6)
      -r url, --registry url
                            Docker Registry from which to pull images (default:
                            docker.io)

    nodebase arguments:
      --node-disks map      Map of node names to block devices (default: None)

    Node groups:
      --nodes node [node ...]
                            Nodes of the nodes group (default: ['node-1',
                            'node-2'])
