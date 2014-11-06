# Copyright (c) 2014 townhallpinball.org
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.provision :shell, path: "vm/bootstrap"
  config.vm.hostname = "no-fear"
  config.ssh.forward_x11 = true
  config.vm.network "forwarded_port", guest: 9000, host: 9000

  config.vm.provider "virtualbox" do |vb|
      vb.name = "no-fear"
      vb.gui = true
      if Vagrant::Util::Platform.windows?
          vb.customize ["modifyvm", :id, "--audio", "dsound",
                        "--audiocontroller", "ac97"]
      else
          vb.customize ["modifyvm", :id, "--audio", "coreaudio",
                        "--audiocontroller", "ac97"]
      end
      config.vm.synced_folder "../pinlib/pinlib", "/usr/local/lib/python2.7/dist-packages/pinlib"
      config.vm.synced_folder "../pinlib/pinws", "/usr/local/lib/python2.7/dist-packages/pinws"
      config.vm.synced_folder "../pinlib/procgame", "/usr/local/lib/python2.7/dist-packages/procgame"
  end
end
