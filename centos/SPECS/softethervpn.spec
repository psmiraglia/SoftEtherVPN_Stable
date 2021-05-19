%define majorversion 4
%define minorversion 34
%define buildversion 9745
%define buildrelease beta

Name:           softethervpn
Version:        %{majorversion}.%{minorversion}.%{buildversion}
Release:        1%{?dist}
Summary:        An Open-Source Free Cross-platform Multi-protocol VPN Program

Group:          Applications/Internet
License:        GPLv2
URL:            http://www.softether.org/
Source0:        https://github.com/SoftEtherVPN/SoftEtherVPN_Stable/archive/refs/tags/v%{majorversion}.%{minorversion}-%{buildversion}-%{buildrelease}.tar.gz

BuildRequires:  ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRequires:	systemd

Requires(post):		chkconfig
Requires(postun):	initscripts
Requires(preun):	chkconfig
Requires(preun):	initscripts

%description
SoftEther VPN is one of the world's most powerful and easy-to-use multi-protocol VPN software. It runs on Windows, Linux, Mac, FreeBSD, and Solaris.

%prep
%setup -q -n SoftEtherVPN_Stable-%{majorversion}.%{minorversion}-%{buildversion}-%{buildrelease}

%build
cp $RPM_SOURCE_DIR/Makefile Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/usr/bin/
install -m 755 -d %{buildroot}%{_unitdir}
install -m 755 $RPM_SOURCE_DIR/vpnserver $RPM_BUILD_ROOT/usr/bin/vpnserver
install -m 755 $RPM_SOURCE_DIR/vpnbridge $RPM_BUILD_ROOT/usr/bin/vpnbridge
install -m 755 $RPM_SOURCE_DIR/vpnclient $RPM_BUILD_ROOT/usr/bin/vpnclient
install -m 755 $RPM_SOURCE_DIR/vpncmd $RPM_BUILD_ROOT/usr/bin/vpncmd
install -m 755 %{_sourcedir}/softether-vpnbridge.service %{buildroot}%{_unitdir}/softether-vpnbridge.service
install -m 755 %{_sourcedir}/softether-vpnclient.service %{buildroot}%{_unitdir}/softether-vpnclient.service
install -m 755 %{_sourcedir}/softether-vpnserver.service %{buildroot}%{_unitdir}/softether-vpnserver.service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_usr}/bin/vpnserver
%{_usr}/bin/vpnbridge
%{_usr}/bin/vpnclient
%{_usr}/bin/vpncmd
%{_usr}/vpnserver/hamcore.se2
%{_usr}/vpnserver/vpnserver
%{_usr}/vpnbridge/hamcore.se2
%{_usr}/vpnbridge/vpnbridge
%{_usr}/vpnclient/hamcore.se2
%{_usr}/vpnclient/vpnclient
%{_usr}/vpncmd/hamcore.se2
%{_usr}/vpncmd/vpncmd
%{_usr}/vpnserver/
%{_usr}/vpnbridge/
%{_usr}/vpnclient/
%{_usr}/vpncmd/
%{_unitdir}/softether-vpnbridge.service
%{_unitdir}/softether-vpnclient.service
%{_unitdir}/softether-vpnserver.service
#%{_initddir}/vpnserver
%doc AUTHORS.TXT BUILD_UNIX.TXT BUILD_WINDOWS.TXT ChangeLog ChangeLog.txt LICENSE LICENSE.TXT README README.TXT THIRD_PARTY.TXT WARNING.TXT

%post
##/sbin/chkconfig --add vpnserver

#%postun
#if [ "$1" -ge "1" ]; then
#	/sbin/service vpnserver condrestart >/dev/null 2>&1 || :
#fi

%preun
##if [ $1 -eq 0 ]; then
##	/sbin/service vpnserver stop >/dev/null 2>&1
##	/sbin/chkconfig --del vpnserver
##fi

%changelog
* Wed Sep 30 2015 Jeff Tang <mrjefftang@gmail.com> - 4.19.9582-1
- Update upstream to 4.19.9582-beta

* Wed Sep 30 2015 Jeff Tang <mrjefftang@gmail.com> - 4.19.9577-1
- Update upstream to 4.19.9577

* Wed Jan 29 2014 Dexter Ang <thepoch@gmail.com> - 4.04.9412-2
- Made initscript more Fedora/RH-like.
- initscript currently using killall. Need to fix this.

* Tue Jan 21 2014 Dexter Ang <thepoch@gmail.com>
- Initial release

