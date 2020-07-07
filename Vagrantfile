# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.provider "virtualbox" do |vb|
    
    vb.memory = "4096"

  end

  config.vm.box = "ubuntu/bionic64"

  config.vm.network "private_network", ip: "192.168.33.100"
  
  config.vm.provision :docker
  
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml", run: "always"

end
