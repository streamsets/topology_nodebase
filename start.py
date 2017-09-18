# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from clusterdock.models import Cluster, Node

DEFAULT_NAMESPACE = 'clusterdock'


def main(args):
    image = '{}/{}/topology_nodebase:{}'.format(args.registry,
                                                args.namespace or DEFAULT_NAMESPACE,
                                                args.operating_system)

    cluster = Cluster(*[Node(hostname=hostname, group='nodes', image=image)
                        for hostname in args.nodes])
    cluster.start(args.network)
