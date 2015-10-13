# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = '2'

@script = <<SCRIPT
sudo yum install -y rpmdevtools rpm-devel rpm-build mock
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.synced_folder '.', '/opt/rpm'

  config.vm.provider 'virtualbox'
  config.vm.provider 'vmware_fusion'

  config.vm.box = 'bento/centos-7.1'

  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--cpus', 2]
    vb.customize ['modifyvm', :id, '--memory', 2048]
  end

  config.vm.provision 'shell', inline: @script
  config.vm.provision 'shell', path: 'build.sh', privileged: false
end
