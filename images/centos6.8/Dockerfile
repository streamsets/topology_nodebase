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
FROM centos:6.8

# Workaround for https://github.com/CentOS/sig-cloud-instance-images/issues/15.
RUN yum install -y yum-plugin-ovl && \
    yum clean all

# Install useful things that are missing from the centos:6.6 image.
RUN yum install -y openssh-clients \
    openssh-server \
    rsyslog \
    sudo \
    tar \
    wget \
    which && \
    yum clean all

# Add pre-created SSH keys into .ssh folder.
# The ssh keys have been removed from this repository to address security concerns. Please pull the id_rsa and
# id_rsa.pub from Vault and copy them into the ssh folder before building this docker image:
# https://ss-vault.streamsets.net/ui/vault/secrets/automation/list/topology_nodebase/
ADD ssh /root/.ssh/

# Copy public key into authorized_keys and limit access to the private key to ensure SSH can use it.
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/id_rsa

# The official CentOS Docker images retain a lot of things that only apply on a real machine.
# Among the most problematic is starting udev, which was seen to hang when containers were started
# simultaneously. Simple solution (and one done by the lxc-centos.in template) is to simply
# not trigger it. The other is the inclusion of the 90-nproc.conf file, which overrides reasonable
# defaults for things like the maximum number of user processes when running commands as a non-root
# user. Get rid of it (and see tinyurl.com/zqdfzpg). Lastly, we edit /etc/sysconfig/network
# to fix issues with the hostname being overriden from what Docker sets (see
# https://github.com/moby/moby/issues/31199).
RUN sed -i 's|/sbin/start_udev||' /etc/rc.d/rc.sysinit && \
    rm /etc/security/limits.d/90-nproc.conf && \
    sed -i '/HOSTNAME/d' /etc/sysconfig/network

# Disable strict host key checking and set the known hosts file to /dev/null to make
# SSH between containers less of a pain.
RUN sed -i -r "s|\s*Host \*\s*|&\n        StrictHostKeyChecking no|" /etc/ssh/ssh_config && \
    sed -i -r "s|\s*Host \*\s*|&\n        UserKnownHostsFile=/dev/null|" /etc/ssh/ssh_config

CMD ["/sbin/init"]
