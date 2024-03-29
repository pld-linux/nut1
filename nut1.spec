#
# Conditional build:
#
# NOTE: Do not (!!!) upgrade nut above 1.2.3 -- everups.c works better
#		with some EVER upses end compiles with nut up to 1.2.3
#
#		You Have Been Warned
#
Summary:	Network UPS Tools
Summary(pl.UTF-8):	Sieciowe narzędzie do UPS-ów
Name:		nut1
Version:	1.2.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://eu1.networkupstools.org/source/1.2/nut-%{version}.tar.gz
# Source0-md5:	87dd831a819d06904cbe06e70dcf3c2f
Source1:	nut.init
Source2:	nut.sysconfig
Source3:	nut-upsmon.init
Source4:	nut.sysconfig.upsmon
Source5:	http://www.nixz.net/nut/everups.c
# NoSource5-md5:	526bd50f3f5cedf6d60b99998f866b0d
Patch0:		nut-client.patch
Patch1:		nut-datadir.patch
Patch2:		nut-config.patch
URL:		http://www.networkupstools.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gd-devel >= 2.0.15
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.202
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/groupmod
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-scripts
Provides:	group(ups)
Provides:	user(ups)
Obsoletes:	smartupstools
Obsoletes:	nut
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/ups

%description
These programs are part of a developing project to monitor the
assortment of UPSes that are found out there in the field. Many models
have serial serial ports of some kind that allow some form of state
checking. This capability has been harnessed where possible to allow
for safe shutdowns, live status tracking on web pages, and more.

This nut ships with modified everups.c - support for Ever UPS models
(by Mikolaj Tutak <mtutak@eranet.pl>)
This is nut-1 (OLD) version of nut!

%description -l pl.UTF-8
Te programy są częścią projektu do monitorowania wielu UPS-ów w jakimś
otoczeniu. Wiele modeli ma porty szeregowe i pozwala na jakąś formę
sprawdzania stanu. Ta funkcjonalność pozwala na bezpieczne
zatrzymywanie systemów, sprawdzanie stanu zasilania przez WWW i inne.

Ta wersja posiada zmieniony sterownik everups.c - obsługuje zasilacze
firmy Ever UPS models (autorstwa Mikołaja Tutaka <mtutak@eranet.pl>)
To jest nut-1 (stara) wersja of nuta!

%description -l ru.UTF-8
Эти программы - часть проекта по мониторингу различных UPS. У многих
моделей есть сериальные порты, позволяющие проверять состояние этих
UPS. Эта возможность была использована, где это возможно, для
выполнения безопасных остановов компьютеров, отслеживания статуса
через веб и т.п.

%description -l uk.UTF-8
Ці програми є частиною проекту по моніторингу різноманітних UPS.
Багато моделей мають серіальні порти, що дозволять перевіряти стан цих
UPS. Ця можливість була використана, де це можливо, для виконання
безпечних зупинок комп'ютерів, відслідковування статусу через веб,
тощо.

%package common
Summary:	Package with common files for nut daemon and its clients
Summary(pl.UTF-8):	Pakiet z plikami wspólnymi dla demona nut i jego klientów
Group:		Applications/System

%description common
Package with common files for nut daemon and its clients.

%description common -l pl.UTF-8
Pakiet z plikami wspólnymi dla demona nut i jego klientów.

%package client
Summary:	Multi-vendor UPS Monitoring Project Client Utilities
Summary(pl.UTF-8):	Narzędzia klienckie do monitorowania UPS-ów
Summary(uk.UTF-8):	Network UPS Tools - клієнтські утиліти моніторингу
Summary(ru.UTF-8):	Network UPS Tools - клиентские утилиты мониторинга
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-scripts

%description client
This package includes the client utilities that are required to
monitor a UPS that the client host is plugged into but monitored via
serial cable by another host on the network....

%description client -l pl.UTF-8
Ten pakiet zawiera narzędzia kliencie potrzebne do monitorowania UPS-a
do którego podłączony jest komputer kliencki, kiedy kabel szeregowy
UPS-a jest podłączony do innego komputera w sieci.

%description client -l ru.UTF-8
Этот пакет включает клиентские утилиты, необходимые для мониторинга
UPS, к которому клиентский хост имеет доступ, но UPS физически
подключен к другому компьютеру в сети.

%description client -l uk.UTF-8
Цей пакет включає клієнтські утиліти, потрібні для моніторингу UPS, до
якого клієнтський хост має доступ, але UPS фізично підключений до
іншого комп'ютеру в мережі.

%package cgi
Summary:	Multi-vendor UPS Monitoring Project Server - CGI utils
Summary(pl.UTF-8):	Narzędzia CGI do monitorowania UPS-ów
Summary(ru.UTF-8):	Network UPS Tools - CGI утилиты
Summary(uk.UTF-8):	Network UPS Tools - CGI утиліти
Group:		Applications/System
Requires:	%{name}-common = %{version}-%{release}

%description cgi
These programs are part of a developing project to monitor the
assortment of UPSes that are found out there in the field. Many models
have serial serial ports of some kind that allow some form of state
checking. This capability has been harnessed where possible to allow
for safe shutdowns, live status tracking on web pages, and more. This
package contains CGI utils.

%description cgi -l pl.UTF-8
Te programy są częścią projektu do monitorowania wielu UPS-ów w jakimś
otoczeniu. Wiele modeli ma porty szeregowe i pozwala na jakąś formę
sprawdzania stanu. Ta funkcjonalność pozwala na bezpieczne
zatrzymywanie systemów, sprawdzanie stanu zasilania przez WWW i inne.
Ten pakiet zawiera narzędzia CGI.

%description cgi -l ru.UTF-8
Этот пакет включает CGI программы для доступа к информации о статусе
UPS через веб-интерфейс.

%description cgi -l uk.UTF-8
Цей пакет включає CGI програми для доступу до інформації про статус
UPS через веб-інтерфейс.

%package devel
Summary:	Files for NUT clients development
Summary(pl.UTF-8):	Pliki do tworzenia klientów NUT-a
Group:		Development/Libraries
Requires:	openssl-devel >= 0.9.7c
# it does NOT require nut

%description devel
Object file and header for developing NUT clients.

%description devel -l pl.UTF-8
Plik wynikowy oraz nagłówek służące do tworzenia klientów NUT-a.

%prep
%setup -q -n nut-%{version}
#%patch0 -p1
#%patch1 -p1
%patch2 -p1
install %{SOURCE5} drivers/everups.c

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
LDFLAGS="-L%{_prefix}/X11R6/%{_lib}"; export LDFLAGS
%configure \
	%{?with_hidups:--with-linux-hiddev} \
	--with-ssl \
	--with-cgi \
	--with-linux-hiddev=%{_includedir}/linux/hiddev.h \
	--with-statepath=%{_var}/lib/ups \
	--with-drvpath=/lib/nut \
	--with-cgipath=/home/services/httpd/cgi-bin \
	--with-user=ups \
	--with-group=ups
%{__make} all cgi
%{?with_hidups:%{__make} build-usb}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,/etc/{sysconfig,rc.d/init.d},/var/lib/ups} \
	$RPM_BUILD_ROOT{/lib/nut,%{_libdir},%{_includedir}/nut}

%{__make} install install-cgi \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ups
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ups
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/upsmon
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/upsmon

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/*
install conf/*.users conf/*.conf conf/*.html $RPM_BUILD_ROOT%{_sysconfdir}

install clients/upsclient.o common/parseconf.o $RPM_BUILD_ROOT%{_libdir}
install clients/upsclient.h include/parseconf.h $RPM_BUILD_ROOT%{_includedir}/nut

%{?with_hidups:install drivers/hidups $RPM_BUILD_ROOT/lib/nut}

cat > $RPM_BUILD_ROOT/sbin/poweroff-ups << EOF
#!/bin/sh
/etc/rc.d/init.d/ups powerdown
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ "`/usr/bin/getgid ups`" = 121 ]; then
	/usr/sbin/groupmod -g 76 ups
	chgrp ups %{_sysconfdir}/{upsd.conf,ups.conf,upsd.users}
	/usr/sbin/usermod -g 76 ups
fi
%groupadd -g 76 ups
%useradd -u 70 -d /usr/share/empty -s /bin/false -c "UPS Manager User" -g ups ups

%post
/sbin/chkconfig --add ups
if [ -f /var/lock/subsys/ups ]; then
	/etc/rc.d/init.d/ups restart >&2
else
	echo "Run \"/etc/rc.d/init.d/ups start\" to start NUT ups daemon."
fi

%post client
/sbin/chkconfig --add upsmon
if [ -f /var/lock/subsys/upsmon ]; then
	/etc/rc.d/init.d/upsmon restart >&2
else
	echo "Run \"/etc/rc.d/init.d/upsmon start\" to start NUT upsmon daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/ups ]; then
		/etc/rc.d/init.d/ups stop >&2
	fi
	/sbin/chkconfig --del ups
fi

%preun client
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/upsmon ]; then
		/etc/rc.d/init.d/upsmon stop >&2
	fi
	/sbin/chkconfig --del upsmon
fi

%postun
if [ "$1" = "0" ]; then
	%userremove ups
	%groupremove ups
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/upscmd
%attr(755,root,root) %{_bindir}/upslog
%attr(755,root,root) %{_bindir}/upsrw
%attr(755,root,root) %{_sbindir}/upsd
%attr(755,root,root) /sbin/poweroff-ups
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ups
%attr(754,root,root) /etc/rc.d/init.d/ups
%attr(640,root,ups) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/upsd.conf
%attr(640,root,ups) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ups.conf
%attr(640,root,ups) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/upsd.users
%{_mandir}/man5/ups.conf.5*
%{_mandir}/man5/upsd.conf.5*
%{_mandir}/man5/upsd.users.5*
%{_mandir}/man8/[!u]*.8*
%{_mandir}/man8/upscmd.8*
%{_mandir}/man8/upsd.8*
%{_mandir}/man8/upsdrvctl.8*
%{_mandir}/man8/upslog.8*
%{_mandir}/man8/upsrw.8*
%dir %attr(770,root,ups) /var/lib/ups
%dir /lib/nut
%attr(755,root,root) /lib/nut/*

%files common
%defattr(644,root,root,755)
%doc NEWS README CHANGES CREDITS docs
%dir %{_sysconfdir}

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/upsc
%attr(755,root,root) %{_sbindir}/upsmon
%attr(755,root,root) %{_sbindir}/upssched
#%attr(755,root,root) %{_sbindir}/upssched-cmd
%attr(754,root,root) /etc/rc.d/init.d/upsmon
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/upsmon.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/upssched.conf
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/upsmon
%{_mandir}/man5/upsmon.conf.5*
%{_mandir}/man5/upssched.conf.5*
%{_mandir}/man8/upsc.8*
%{_mandir}/man8/upsmon.8*
%{_mandir}/man8/upssched.8*

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) /home/services/httpd/cgi-bin/*.cgi
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hosts.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/upsset.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.html
%{_mandir}/man5/hosts.conf.5*
%{_mandir}/man5/upsset.conf.5*
%{_mandir}/man5/upsstats.html.5*
%{_mandir}/man8/upsimage.cgi.8*
%{_mandir}/man8/upsset.cgi.8*
%{_mandir}/man8/upsstats.cgi.8*

%files devel
%defattr(644,root,root,755)
%{_libdir}/upsclient.o
%{_libdir}/parseconf.o
%{_includedir}/nut
