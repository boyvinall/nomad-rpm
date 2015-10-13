#!/bin/bash -x
rm -rf /home/vagrant/rpmbuild
rpmdev-setuptree
[ -L /home/vagrant/rpmbuild/SPECS/nomad.spec ] || ln -s /opt/rpm/SPECS/nomad.spec /home/vagrant/rpmbuild/SPECS/
for f in `find /opt/rpm/SOURCES -type f`; do
  [ -L /home/vagrant/rpmbuild/SOURCES/`basename $f` ] || ln -s $f /home/vagrant/rpmbuild/SOURCES/
done
spectool -g -R /home/vagrant/rpmbuild/SPECS/nomad.spec
rpmbuild -ba /home/vagrant/rpmbuild/SPECS/nomad.spec
cp /home/vagrant/rpmbuild/RPMS/x86_64/nomad*.rpm /opt/rpm
