Name:           nomad
Version:        0.9.0
Release:        1%{?dist}
Summary:        A Distributed, Highly Available, Datacenter-Aware Scheduler

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            https://www.nomadproject.io/
Source0:        https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.json
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
BuildRequires:  systemd-units
Requires:       systemd
%endif
Requires(pre): shadow-utils

%description
A Distributed, Highly Available, Datacenter-Aware Scheduler

%prep
%setup -c

%install
mkdir -p %{buildroot}/%{_bindir}
cp nomad %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
cp %{SOURCE3} %{buildroot}/%{_sysconfdir}/%{name}/nomad.json.template
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
mkdir -p %{buildroot}/%{_unitdir}
cp %{SOURCE1} %{buildroot}/%{_unitdir}/
%endif

%pre
getent group nomad >/dev/null || groupadd -r nomad
getent passwd nomad >/dev/null || \
    useradd -r -g nomad -d /var/lib/nomad -s /sbin/nologin \
    -c "nomadproject.io user" nomad
exit 0

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %attr(755, root, root) %{_sysconfdir}/%{name}
%dir %attr(750, nomad, nomad) %{_sharedstatedir}/%{name}
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%endif
%attr(755, root, root) %{_bindir}/%{name}
%attr(755, root, root) %{_sysconfdir}/%{name}/nomad.json.template
%attr(755, root, root) %{_sysconfdir}/sysconfig/%{name}

%doc


%changelog
* Wed Feb 05 2019 KelnMaari <zu_krein@protonmail.com>
* Update spec to version 0.8.7

* Tue Oct 13 2015 Matt <matt.vinall@imgtec.com>
* initial version
