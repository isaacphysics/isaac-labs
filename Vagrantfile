Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", type: "dhcp"
  config.vm.synced_folder ".", "/isaac-labs"

  # For Jekyll
  config.vm.network "forwarded_port", guest: 4000, host: 4000

   config.vm.provider "virtualbox" do |vb|
     # Display the VirtualBox GUI when booting the machine
     # vb.gui = true
  
     # Customize the amount of memory on the VM:
     vb.memory = "4096"
     vb.cpus = 2
     vb.name = "isaac-labs-dev"
   end

  config.vm.provision :shell, path: "vagrant-bootstrap.sh"

  config.ssh.forward_agent = true
  
end
