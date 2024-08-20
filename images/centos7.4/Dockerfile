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

FROM centos:7.4.1708
ENV container docker

# Update baseurl on all repos files
RUN sed -i -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" /etc/yum.repos.d/CentOS-*
RUN sed -i -e "s|mirrorlist|#mirrorlist|g" /etc/yum.repos.d/CentOS-*

# Delete a number of unit files which might cause issues.
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# Install useful things that are missing from the centos:7.4.1708 image.
RUN yum install -y initscripts \
    openssh-clients \
    openssh-server \
    rsyslog \
    sudo \
    wget \
    which && \
    yum clean all

# Add pre-created SSH keys into .ssh folder.
ADD ssh /root/.ssh/

# Copy public key into authorized_keys and limit access to the private key to ensure SSH can use it.
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/id_rsa

# The official CentOS Docker images retain the inclusion of the 20-nproc.conf file that only applies on a real machine.
# This file overrides reasonable defaults for things like the maximum number of user processes when running commands
# as a non-root user. Get rid of it (and see tinyurl.com/zqdfzpg).
RUN rm /etc/security/limits.d/20-nproc.conf

# Disable strict host key checking to /dev/null to make SSH between containers less of a pain.
RUN sed -i -r "s|^Host \*\s*|&\n        StrictHostKeyChecking no|" /etc/ssh/ssh_config

CMD ["/usr/sbin/init"]
