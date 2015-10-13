# RPM Spec for Nomad

Tries to follow the [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines) from Fedora.

* Binary: `/usr/bin/nomad`
* Config: `/etc/nomad/`

Heavily borrowed from https://github.com/stevendborrelli/consul-template-rpm.

# Build

If you have [vagrant](https://www.vagrantup.com/) installed, then just clone this repo and `vagrant up`.

If not, build the RPM as a non-root user from your home directory:

* Check out this repo. Seriously - check it out. Nice.
    ```
    git clone <this_repo_url>
    ```

* Install `rpmdevtools` and `mock`.
    ```
    sudo yum install rpmdevtools mock
    ```

* Set up your rpmbuild directory tree.
    ```
    rpmdev-setuptree
    ```

* Link the spec file and sources.
    ```
    ln -s $HOME/nomad-rpm/SPECS/nomad.spec rpmbuild/SPECS/
    find $HOME/nomad-rpm/SOURCES -type f -exec ln -s {} rpmbuild/SOURCES/ \;
    ```

* Download remote source files
    ```
    spectool -g -R rpmbuild/SPECS/nomad.spec
    ```

* Build the RPM
    ```
    rpmbuild -ba rpmbuild/SPECS/nomad.spec
    ```

## Result

One RPM for the Nomad binary.

# Run

* Install the RPM.
* Put config files in `/etc/nomad/`.
* Start the service and tail the logs `systemctl start nomad.service` and `journalctl -f`.
  * To enable at reboot `systemctl enable nomad.service`.

## Config

Config files are loaded in lexicographical order from the `config` dir. Some
sample configs are provided.

# More info

See the [nomadproject.io](http://www.nomadproject.io) website.
