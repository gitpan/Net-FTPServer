# Automatically generated by Net-FTPServer.spec.PL

%define perlsitearch %(perl -e 'use Config; print $Config{installsitearch}')
%define perlsitelib %(perl -e 'use Config; print $Config{installsitelib}')
%define perlman1dir %(perl -e 'use Config; print $Config{installman1dir}')
%define perlman3dir %(perl -e 'use Config; print $Config{installman3dir}')
%define perlversion %(perl -e 'use Config; print $Config{version}')

Summary: Net::FTPServer - an extensible, secure FTP server
Name: perl-Net-FTPServer
Version: 1.112
Release: 1
Copyright: GPL
Group: Applications/Internet
Source: Net-FTPServer-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: perl-Authen-PAM >= 0.12
BuildRequires: perl-BSD-Resource >= 1.08
BuildRequires: perl-File-Sync >= 0.09
BuildRequires: perl-IO-stringy >= 1.220
BuildRequires: perl >= %{perlversion}
Requires: perl-Authen-PAM >= 0.12
Requires: perl-BSD-Resource >= 1.08
Requires: perl-File-Sync >= 0.09
Requires: perl-IO-stringy >= 1.220
Requires: perl >= %{perlversion}


%description
Biblio@Tech Net::FTPServer - A full-featured, secure, extensible
and configurable Perl FTP server.


%prep
%setup -q -n Net-FTPServer-%{version}


%build
NET_FTPSERVER_NO_SLEEP=1 perl Makefile.PL
make
make test


%install
rm -rf $RPM_BUILD_ROOT
make NOCONF=1 PREFIX=$RPM_BUILD_ROOT/usr install

mkdir $RPM_BUILD_ROOT/etc
install -c -m 0644 ftpd.conf $RPM_BUILD_ROOT/etc


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING FAQ INSTALL README TODO doc/*
%{perlsitearch}/auto/Net/FTPServer/
%{perlsitearch}/Net/FTPServer.pm
%{perlsitearch}/Net/FTPServer/
%{perlman3dir}/*.3*
/usr/sbin/*.pl
%config(noreplace) /etc/ftpd.conf


%changelog
* Fri Dec 28 2001 Richard Jones <rich@annexia.org>
- Better handling of different Perl versions. RPM contains documentation,
- config file and start-up scripts.
* Tue Feb 15 2001 Rob Brown <rbrown@about-inc.com>
- Generalized files - works with Perl 5.6 as well as with Perl 5.005
* Tue Feb 08 2001 Richard Jones <rich@annexia.org>
- initial creation
