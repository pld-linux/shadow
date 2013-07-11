#
# TODO
# - handle conflicting files:
#error: Install/Erase problems:
#        file /usr/share/man/cs/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /usr/share/man/de/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /usr/share/man/fr/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /usr/share/man/it/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /usr/share/man/ja/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /usr/share/man/ko/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /usr/share/man/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /usr/share/man/pl/man1/groups.1.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package coreutils-8.20-2.x86_64
#        file /sbin/nologin from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package util-linux-2.22.2-4.x86_64
#        file /usr/share/man/man8/nologin.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package util-linux-2.22.2-4.x86_64
#        file /usr/share/man/cs/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/fr/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/hu/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/it/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/ja/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/pl/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/ru/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/sv/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-tools-2.88-13.x86_64
#        file /usr/share/man/man8/lastlog.8.gz from install of shadow-4.1.5.1-0.1.x86_64 conflicts with file from package SysVinit-2.88-13.x86_64
# - /etc/default/useradd is very outdated:
# gpasswd -M chef_server chef_server
#configuration error - unknown item 'FAILLOG_ENAB' (notify administrator)
#configuration error - unknown item 'LASTLOG_ENAB' (notify administrator)
#configuration error - unknown item 'MAIL_CHECK_ENAB' (notify administrator)
#configuration error - unknown item 'OBSCURE_CHECKS_ENAB' (notify administrator)
#configuration error - unknown item 'PORTTIME_CHECKS_ENAB' (notify administrator)
#configuration error - unknown item 'QUOTAS_ENAB' (notify administrator)
#configuration error - unknown item 'MOTD_FILE' (notify administrator)
#configuration error - unknown item 'FTMP_FILE' (notify administrator)
#configuration error - unknown item 'NOLOGINS_FILE' (notify administrator)
#configuration error - unknown item 'ENV_HZ' (notify administrator)
#configuration error - unknown item 'PASS_MIN_LEN' (notify administrator)
#configuration error - unknown item 'SU_WHEEL_ONLY' (notify administrator)
#configuration error - unknown item 'CRACKLIB_DICTPATH' (notify administrator)
#configuration error - unknown item 'PASS_CHANGE_TRIES' (notify administrator)
#configuration error - unknown item 'PASS_ALWAYS_WARN' (notify administrator)
#configuration error - unknown item 'CHFN_AUTH' (notify administrator)
#configuration error - unknown item 'ENVIRON_FILE' (notify administrator)
# - sync pam files from pwdutils

# Conditional build:
%bcond_without	selinux		# build without SE-Linux support
%bcond_with	shared		# build with shared libshadow (linking with selinux is broken)
#
Summary:	Shadow password file utilities for Linux
Summary(de.UTF-8):	Shadow-Paßwortdatei-Dienstprogramme für Linux
Summary(es.UTF-8):	Utilitarios para el archivo de contraseñas Shadow
Summary(fr.UTF-8):	Fichiers utilitaires pour Shadow password pour Linux
Summary(pl.UTF-8):	Narzędzia do obsługi mechanizmu ukrytych haseł
Summary(pt_BR.UTF-8):	Utilitários para o arquivo de senhas Shadow
Summary(tr.UTF-8):	Gölge parola dosyası araçları
Name:		shadow
Version:	4.1.5.1
#BuildRequires:	useradd -g is broken, use pwdutils, or fix it:
# http://zie.pg.gda.pl/mailman/pipermail/shadow/2006-September/000395.html
Release:	0.1
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	http://pkg-shadow.alioth.debian.org/releases/shadow-%{version}.tar.bz2
# Source0-md5:	a00449aa439c69287b6d472191dc2247
Source1:	http://pkg-shadow.alioth.debian.org/releases/shadow-%{version}.tar.bz2.sig
# Source1-md5:	f16f31f6f5a607b1ffb1aa1aac4c37f2
Source2:	%{name}-login.defs
Source3:	%{name}.useradd
Source10:	chage.pamd
Source11:	chfn.pamd
Source12:	chgpasswd.pamd
Source13:	chpasswd.pamd
Source14:	chsh.pamd
Source15:	groupadd.pamd
Source16:	groupdel.pamd
Source17:	groupmems.pamd
Source18:	groupmod.pamd
Source19:	newusers.pamd
Source20:	passwd.pamd
Source21:	useradd.pamd
Source22:	userdel.pamd
Source23:	usermod.pamd
Patch0:		%{name}-pld.patch
Patch1:		%{name}-goodname.patch
URL:		http://pkg-shadow.alioth.debian.org/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	audit-libs-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.0
BuildRequires:	gettext-devel >= 0.12.1
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool
BuildRequires:	pam-devel
Requires:	pam >= 0.99.7.1
# to force proper coreutils version, so "groups" command exists
Requires:	/usr/bin/groups
Provides:	passwd
Provides:	shadow-utils
Obsoletes:	passwd
Obsoletes:	shadow-extras
Obsoletes:	shadow-utils
Obsoletes:	pwdutils
Conflicts:	util-linux < 2.12-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes the programs necessary to convert standard UNIX
password files to the shadow password format, as well as programs for
command-line management of the user's accounts.
- pwconv - converts everything to the shadow password format,
- pwunconv - unconverts from shadow password, generating a file in the
  current directory called npasswd that is a standard UNIX password
  file,
- pwck - checks the integrity of the password and shadow files,
- lastlog - prints out the last login times of all users,
- useradd, userdel, usermod - for accounts management,
- groupadd, groupdel, groupmod - for group management.

A number of man pages are also included that relate to these
utilities, and shadow passwords in general.

%description -l es.UTF-8
Este paquete incluye los programas necesarios para convertir Archivos
padrón UNIX de contraseña al formato shadow.
- pwconv5 - convierte todo al formato de contraseñas del shadow,
- pwunconv - deshace la conversión de contraseñas shadow, creando un
  archivo en el directorio corriente llamado npasswd que es el archivo
  padrón UNIX de contraseña,
- pwck - chequea la integridad de la contraseña y de los archivos
  shadow,
- lastlog enseña el último momento de login de todos los usuarios.
  Están también incluidas, en general, varias páginas de manual sobre
  estos utilitarios y contraseñas shadow.

%description -l pl.UTF-8
Pakiet zawiera programy do obsługi mechanizmu ukrytych haseł (shadow
password). Znajdują się w nim programy do konwersji standardowego
pliku haseł do wersji shadow password a także programy do zarządzania
kontami użytkowników w systemie:
- pwconv - konwertuje do formatu shadow password
- pwunconv - konwertuje z shadow password do formatu standardowego
  pliku haseł. W bieżącym katalogu tworzy plik npasswd będący
  standardowym plikiem z hasłami,
- lastlog - wyświetla czas logowania użytkowników,
- useradd, userdel, usermod - do zarządzania kontami użytkowników,
- groupadd, groupdel, groupmod - do zarządzania grupami.

Ostrzeżenie:

Programy znajdujące się w tym pakiecie są niezbędne do prawidłowej
pracy systemu i podobnie jak pakiet z bibliotekami systemowymi (glibc)
nigdy nie powinien zostać odinstalowany!

%description -l pt_BR.UTF-8
Este pacote inclui os programas necessários para converter
arquivos-padrão UNIX de senha para o formato shadow.
- pwconv - converte tudo para o formato de senhas do shadow,
- pwunconv - desconverte senhas shadow, gerando um arquivo no
  diretório corrente chamado npasswd que é o arquivo-padrão UNIX de
  senha,
- pwck - checa a integridade da senha e dos arquivos shadow,
- lastlog - mostra o último momento de login de todos os usuários.

Várias páginas de manual estão também incluídas sobre estes
utilitários e senhas shadow em geral.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	%{?with_shared:--enable-shared --disable-static} \
	--without-libcrack \
	--without-tcb \
	--with-sha-crypt \
	--with-nscd \
	--with-audit \
	--with-acl \
	--with-attr \
	--with-libpam \
	--enable-nls \
	--enable-shadowgrp \
	%{?with_selinux:--with-selinux} \
	--with-group-name-max-length=32

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sysconfdir}/{default,pam.d,security,skel/tmp}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/login.defs
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/default/useradd

install %{SOURCE10} $RPM_BUILD_ROOT/etc/pam.d/chage
install %{SOURCE11} $RPM_BUILD_ROOT/etc/pam.d/chfn
install %{SOURCE12} $RPM_BUILD_ROOT/etc/pam.d/chgpasswd
install %{SOURCE13} $RPM_BUILD_ROOT/etc/pam.d/chpasswd
install %{SOURCE14} $RPM_BUILD_ROOT/etc/pam.d/chsh
install %{SOURCE15} $RPM_BUILD_ROOT/etc/pam.d/groupadd
install %{SOURCE16} $RPM_BUILD_ROOT/etc/pam.d/groupdel
install %{SOURCE17} $RPM_BUILD_ROOT/etc/pam.d/groupmems
install %{SOURCE18} $RPM_BUILD_ROOT/etc/pam.d/groupmod
install %{SOURCE19} $RPM_BUILD_ROOT/etc/pam.d/newusers
install %{SOURCE20} $RPM_BUILD_ROOT/etc/pam.d/passwd
install %{SOURCE21} $RPM_BUILD_ROOT/etc/pam.d/useradd
install %{SOURCE22} $RPM_BUILD_ROOT/etc/pam.d/userdel
install %{SOURCE23} $RPM_BUILD_ROOT/etc/pam.d/usermod

> $RPM_BUILD_ROOT%{_sysconfdir}/shadow
> $RPM_BUILD_ROOT/etc/security/chfn.allow
> $RPM_BUILD_ROOT/etc/security/chsh.allow

%{__rm} $RPM_BUILD_ROOT/{etc/pam.d,bin}/{login,su}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{,*/}man1/{login,su}.1*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{,*/}man3/*.3*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{?with_shared:/sbin/ldconfig}
if [ ! -f /etc/shadow ]; then
	%{_sbindir}/pwconv
fi

%{?with_shared:%postun -p /sbin/ldconfig}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS TODO doc/{HOWTO,WISHLIST}
%attr(750,root,root) %dir %{_sysconfdir}/default
%attr(640,root,root) %config %verify(not md5 mtime size) %{_sysconfdir}/default/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chage
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chfn
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chgpasswd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chpasswd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chsh
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/groupadd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/groupdel
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/groupmems
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/groupmod
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/newusers
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/passwd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/useradd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/userdel
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/usermod

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/chfn.allow
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/chsh.allow
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/login.defs
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/shadow
%dir /etc/skel
%dir /etc/skel/tmp
%{?with_shared:%attr(755,root,root) %{_libdir}/lib*.so.*.*}
%attr(755,root,root) /bin/groups
%attr(755,root,root) /sbin/nologin
%attr(755,root,root) %{_bindir}/chage
%attr(4755,root,root) %{_bindir}/chfn
%attr(4755,root,root) %{_bindir}/chsh
%attr(4755,root,root) %{_bindir}/expiry
%attr(755,root,root) %{_bindir}/faillog
%attr(4755,root,root) %{_bindir}/gpasswd
%attr(755,root,root) %{_bindir}/lastlog
%attr(755,root,root) %{_bindir}/newgrp
%attr(4755,root,root) %{_bindir}/passwd
%attr(755,root,root) %{_bindir}/sg
%attr(755,root,root) %{_sbindir}/chgpasswd
%attr(755,root,root) %{_sbindir}/chpasswd
%attr(755,root,root) %{_sbindir}/groupadd
%attr(755,root,root) %{_sbindir}/groupdel
%attr(755,root,root) %{_sbindir}/groupmems
%attr(755,root,root) %{_sbindir}/groupmod
%attr(755,root,root) %{_sbindir}/grpck
%attr(755,root,root) %{_sbindir}/grpconv
%attr(755,root,root) %{_sbindir}/grpunconv
%attr(755,root,root) %{_sbindir}/logoutd
%attr(755,root,root) %{_sbindir}/newusers
%attr(755,root,root) %{_sbindir}/pwck
%attr(755,root,root) %{_sbindir}/pwconv
%attr(755,root,root) %{_sbindir}/pwunconv
%attr(755,root,root) %{_sbindir}/useradd
%attr(755,root,root) %{_sbindir}/userdel
%attr(755,root,root) %{_sbindir}/usermod
%attr(755,root,root) %{_sbindir}/vigr
%attr(755,root,root) %{_sbindir}/vipw
%{_mandir}/man1/chage.1*
%{_mandir}/man1/chfn.1*
%{_mandir}/man1/chsh.1*
%{_mandir}/man1/expiry.1*
%{_mandir}/man1/gpasswd.1*
%{_mandir}/man1/groups.1*
%{_mandir}/man1/newgrp.1*
%{_mandir}/man1/passwd.1*
%{_mandir}/man1/sg.1*
%{_mandir}/man5/faillog.5*
%{_mandir}/man5/gshadow.5*
%{_mandir}/man5/login.defs.5*
%{_mandir}/man5/passwd.5*
%{_mandir}/man5/shadow.5*
%{_mandir}/man5/suauth.5*
%{_mandir}/man8/chgpasswd.8*
%{_mandir}/man8/chpasswd.8*
%{_mandir}/man8/faillog.8*
%{_mandir}/man8/groupadd.8*
%{_mandir}/man8/groupdel.8*
%{_mandir}/man8/groupmems.8*
%{_mandir}/man8/groupmod.8*
%{_mandir}/man8/grpck.8*
%{_mandir}/man8/grpconv.8*
%{_mandir}/man8/grpunconv.8*
%{_mandir}/man8/lastlog.8*
%{_mandir}/man8/logoutd.8*
%{_mandir}/man8/newusers.8*
%{_mandir}/man8/nologin.8*
%{_mandir}/man8/pwck.8*
%{_mandir}/man8/pwconv.8*
%{_mandir}/man8/pwunconv.8*
%{_mandir}/man8/useradd.8*
%{_mandir}/man8/userdel.8*
%{_mandir}/man8/usermod.8*
%{_mandir}/man8/vigr.8*
%{_mandir}/man8/vipw.8*

%lang(cs) %{_mandir}/cs/man1/expiry.1*
%lang(cs) %{_mandir}/cs/man1/gpasswd.1*
%lang(cs) %{_mandir}/cs/man1/groups.1*
%lang(cs) %{_mandir}/cs/man5/faillog.5*
%lang(cs) %{_mandir}/cs/man5/gshadow.5*
%lang(cs) %{_mandir}/cs/man5/passwd.5*
%lang(cs) %{_mandir}/cs/man5/shadow.5*
%lang(cs) %{_mandir}/cs/man8/faillog.8*
%lang(cs) %{_mandir}/cs/man8/groupadd.8*
%lang(cs) %{_mandir}/cs/man8/groupdel.8*
%lang(cs) %{_mandir}/cs/man8/groupmod.8*
%lang(cs) %{_mandir}/cs/man8/grpck.8*
%lang(cs) %{_mandir}/cs/man8/lastlog.8*
%lang(cs) %{_mandir}/cs/man8/nologin.8*
%lang(cs) %{_mandir}/cs/man8/vipw.8*

%lang(da) %{_mandir}/da/man1/chfn.1*
%lang(da) %{_mandir}/da/man1/groups.1*
%lang(da) %{_mandir}/da/man1/newgrp.1*
%lang(da) %{_mandir}/da/man1/sg.1*
%lang(da) %{_mandir}/da/man5/gshadow.5*
%lang(da) %{_mandir}/da/man8/groupdel.8*
%lang(da) %{_mandir}/da/man8/logoutd.8*
%lang(da) %{_mandir}/da/man8/nologin.8*
%lang(da) %{_mandir}/da/man8/vigr.8
%lang(da) %{_mandir}/da/man8/vipw.8*

%lang(de) %{_mandir}/de/man1/chage.1*
%lang(de) %{_mandir}/de/man1/chfn.1*
%lang(de) %{_mandir}/de/man1/chsh.1*
%lang(de) %{_mandir}/de/man1/expiry.1*
%lang(de) %{_mandir}/de/man1/gpasswd.1*
%lang(de) %{_mandir}/de/man1/groups.1*
%lang(de) %{_mandir}/de/man1/newgrp.1*
%lang(de) %{_mandir}/de/man1/passwd.1*
%lang(de) %{_mandir}/de/man1/sg.1*
%lang(de) %{_mandir}/de/man5/faillog.5*
%lang(de) %{_mandir}/de/man5/gshadow.5*
%lang(de) %{_mandir}/de/man5/login.defs.5*
%lang(de) %{_mandir}/de/man5/passwd.5*
%lang(de) %{_mandir}/de/man5/shadow.5*
%lang(de) %{_mandir}/de/man5/suauth.5*
%lang(de) %{_mandir}/de/man8/chgpasswd.8*
%lang(de) %{_mandir}/de/man8/chpasswd.8*
%lang(de) %{_mandir}/de/man8/faillog.8*
%lang(de) %{_mandir}/de/man8/groupadd.8*
%lang(de) %{_mandir}/de/man8/groupdel.8*
%lang(de) %{_mandir}/de/man8/groupmems.8*
%lang(de) %{_mandir}/de/man8/groupmod.8*
%lang(de) %{_mandir}/de/man8/grpck.8*
%lang(de) %{_mandir}/de/man8/grpconv.8*
%lang(de) %{_mandir}/de/man8/grpunconv.8*
%lang(de) %{_mandir}/de/man8/lastlog.8*
%lang(de) %{_mandir}/de/man8/logoutd.8*
%lang(de) %{_mandir}/de/man8/newusers.8*
%lang(de) %{_mandir}/de/man8/nologin.8*
%lang(de) %{_mandir}/de/man8/pwck.8*
%lang(de) %{_mandir}/de/man8/pwconv.8*
%lang(de) %{_mandir}/de/man8/pwunconv.8*
%lang(de) %{_mandir}/de/man8/useradd.8*
%lang(de) %{_mandir}/de/man8/userdel.8*
%lang(de) %{_mandir}/de/man8/usermod.8*
%lang(de) %{_mandir}/de/man8/vigr.8*
%lang(de) %{_mandir}/de/man8/vipw.8*

%lang(fi) %{_mandir}/fi/man1/chfn.1*
%lang(fi) %{_mandir}/fi/man1/chsh.1*

%lang(fr) %{_mandir}/fr/man1/chage.1*
%lang(fr) %{_mandir}/fr/man1/chfn.1*
%lang(fr) %{_mandir}/fr/man1/chsh.1*
%lang(fr) %{_mandir}/fr/man1/expiry.1*
%lang(fr) %{_mandir}/fr/man1/gpasswd.1*
%lang(fr) %{_mandir}/fr/man1/groups.1*
%lang(fr) %{_mandir}/fr/man1/newgrp.1*
%lang(fr) %{_mandir}/fr/man1/passwd.1*
%lang(fr) %{_mandir}/fr/man1/sg.1*
%lang(fr) %{_mandir}/fr/man5/faillog.5*
%lang(fr) %{_mandir}/fr/man5/gshadow.5*
%lang(fr) %{_mandir}/fr/man5/login.defs.5*
%lang(fr) %{_mandir}/fr/man5/passwd.5*
%lang(fr) %{_mandir}/fr/man5/shadow.5*
%lang(fr) %{_mandir}/fr/man5/suauth.5*
%lang(fr) %{_mandir}/fr/man8/chgpasswd.8*
%lang(fr) %{_mandir}/fr/man8/chpasswd.8*
%lang(fr) %{_mandir}/fr/man8/faillog.8*
%lang(fr) %{_mandir}/fr/man8/groupadd.8*
%lang(fr) %{_mandir}/fr/man8/groupdel.8*
%lang(fr) %{_mandir}/fr/man8/groupmems.8*
%lang(fr) %{_mandir}/fr/man8/groupmod.8*
%lang(fr) %{_mandir}/fr/man8/grpck.8*
%lang(fr) %{_mandir}/fr/man8/grpconv.8*
%lang(fr) %{_mandir}/fr/man8/grpunconv.8*
%lang(fr) %{_mandir}/fr/man8/lastlog.8*
%lang(fr) %{_mandir}/fr/man8/logoutd.8*
%lang(fr) %{_mandir}/fr/man8/newusers.8*
%lang(fr) %{_mandir}/fr/man8/nologin.8*
%lang(fr) %{_mandir}/fr/man8/pwck.8*
%lang(fr) %{_mandir}/fr/man8/pwconv.8*
%lang(fr) %{_mandir}/fr/man8/pwunconv.8*
%lang(fr) %{_mandir}/fr/man8/useradd.8*
%lang(fr) %{_mandir}/fr/man8/userdel.8*
%lang(fr) %{_mandir}/fr/man8/usermod.8*
%lang(fr) %{_mandir}/fr/man8/vigr.8*
%lang(fr) %{_mandir}/fr/man8/vipw.8*

%lang(hu) %{_mandir}/hu/man1/passwd.1*
%lang(hu) %{_mandir}/hu/man1/chsh.1*
%lang(hu) %{_mandir}/hu/man1/gpasswd.1*
%lang(hu) %{_mandir}/hu/man1/newgrp.1*
%lang(hu) %{_mandir}/hu/man1/sg.1*
%lang(hu) %{_mandir}/hu/man5/passwd.5*
%lang(hu) %{_mandir}/hu/man8/lastlog.8*
%lang(hu) %{_mandir}/hu/man1/groups.1*

%lang(id) %{_mandir}/id/man1/chsh.1*
%lang(id) %{_mandir}/id/man8/useradd.8*

%lang(it) %{_mandir}/it/man1/chage.1*
%lang(it) %{_mandir}/it/man1/chfn.1*
%lang(it) %{_mandir}/it/man1/chsh.1*
%lang(it) %{_mandir}/it/man1/expiry.1*
%lang(it) %{_mandir}/it/man1/gpasswd.1*
%lang(it) %{_mandir}/it/man1/groups.1*
%lang(it) %{_mandir}/it/man1/newgrp.1*
%lang(it) %{_mandir}/it/man1/passwd.1*
%lang(it) %{_mandir}/it/man1/sg.1*
%lang(it) %{_mandir}/it/man5/faillog.5*
%lang(it) %{_mandir}/it/man5/gshadow.5*
%lang(it) %{_mandir}/it/man5/login.defs.5*
%lang(it) %{_mandir}/it/man5/passwd.5*
%lang(it) %{_mandir}/it/man5/shadow.5*
%lang(it) %{_mandir}/it/man5/suauth.5*
%lang(it) %{_mandir}/it/man8/chgpasswd.8*
%lang(it) %{_mandir}/it/man8/chpasswd.8*
%lang(it) %{_mandir}/it/man8/faillog.8*
%lang(it) %{_mandir}/it/man8/groupadd.8*
%lang(it) %{_mandir}/it/man8/groupdel.8*
%lang(it) %{_mandir}/it/man8/groupmems.8*
%lang(it) %{_mandir}/it/man8/groupmod.8*
%lang(it) %{_mandir}/it/man8/grpck.8*
%lang(it) %{_mandir}/it/man8/grpconv.8*
%lang(it) %{_mandir}/it/man8/grpunconv.8*
%lang(it) %{_mandir}/it/man8/lastlog.8*
%lang(it) %{_mandir}/it/man8/logoutd.8*
%lang(it) %{_mandir}/it/man8/newusers.8*
%lang(it) %{_mandir}/it/man8/nologin.8*
%lang(it) %{_mandir}/it/man8/pwck.8*
%lang(it) %{_mandir}/it/man8/pwconv.8*
%lang(it) %{_mandir}/it/man8/pwunconv.8*
%lang(it) %{_mandir}/it/man8/useradd.8*
%lang(it) %{_mandir}/it/man8/userdel.8*
%lang(it) %{_mandir}/it/man8/usermod.8*
%lang(it) %{_mandir}/it/man8/vigr.8*
%lang(it) %{_mandir}/it/man8/vipw.8*

%lang(ja) %{_mandir}/ja/man1/chage.1*
%lang(ja) %{_mandir}/ja/man1/chfn.1*
%lang(ja) %{_mandir}/ja/man1/chsh.1*
%lang(ja) %{_mandir}/ja/man1/expiry.1*
%lang(ja) %{_mandir}/ja/man1/gpasswd.1*
%lang(ja) %{_mandir}/ja/man1/groups.1*
%lang(ja) %{_mandir}/ja/man1/newgrp.1*
%lang(ja) %{_mandir}/ja/man1/passwd.1*
%lang(ja) %{_mandir}/ja/man1/sg.1*
%lang(ja) %{_mandir}/ja/man5/faillog.5*
%lang(ja) %{_mandir}/ja/man5/login.defs.5*
%lang(ja) %{_mandir}/ja/man5/passwd.5*
%lang(ja) %{_mandir}/ja/man5/shadow.5*
%lang(ja) %{_mandir}/ja/man5/suauth.5*
%lang(ja) %{_mandir}/ja/man8/chpasswd.8*
%lang(ja) %{_mandir}/ja/man8/faillog.8*
%lang(ja) %{_mandir}/ja/man8/groupadd.8*
%lang(ja) %{_mandir}/ja/man8/groupdel.8*
%lang(ja) %{_mandir}/ja/man8/groupmod.8*
%lang(ja) %{_mandir}/ja/man8/grpck.8*
%lang(ja) %{_mandir}/ja/man8/grpconv.8*
%lang(ja) %{_mandir}/ja/man8/grpunconv.8*
%lang(ja) %{_mandir}/ja/man8/lastlog.8*
%lang(ja) %{_mandir}/ja/man8/logoutd.8*
%lang(ja) %{_mandir}/ja/man8/newusers.8*
%lang(ja) %{_mandir}/ja/man8/pwck.8*
%lang(ja) %{_mandir}/ja/man8/pwconv.8*
%lang(ja) %{_mandir}/ja/man8/pwunconv.8*
%lang(ja) %{_mandir}/ja/man8/useradd.8*
%lang(ja) %{_mandir}/ja/man8/userdel.8*
%lang(ja) %{_mandir}/ja/man8/usermod.8*
%lang(ja) %{_mandir}/ja/man8/vigr.8*
%lang(ja) %{_mandir}/ja/man8/vipw.8*

%lang(ko) %{_mandir}/ko/man1/chfn.1*
%lang(ko) %{_mandir}/ko/man1/chsh.1*
%lang(ko) %{_mandir}/ko/man1/groups.1*
%lang(ko) %{_mandir}/ko/man5/passwd.5*
%lang(ko) %{_mandir}/ko/man8/vigr.8*
%lang(ko) %{_mandir}/ko/man8/vipw.8*

%lang(pl) %{_mandir}/pl/man1/chage.1*
%lang(pl) %{_mandir}/pl/man1/chsh.1*
%lang(pl) %{_mandir}/pl/man1/expiry.1*
%lang(pl) %{_mandir}/pl/man1/groups.1*
%lang(pl) %{_mandir}/pl/man1/newgrp.1*
%lang(pl) %{_mandir}/pl/man1/sg.1*
%lang(pl) %{_mandir}/pl/man5/faillog.5*
%lang(pl) %{_mandir}/pl/man8/faillog.8*
%lang(pl) %{_mandir}/pl/man8/groupadd.8*
%lang(pl) %{_mandir}/pl/man8/groupdel.8*
%lang(pl) %{_mandir}/pl/man8/groupmems.8*
%lang(pl) %{_mandir}/pl/man8/groupmod.8*
%lang(pl) %{_mandir}/pl/man8/grpck.8*
%lang(pl) %{_mandir}/pl/man8/lastlog.8*
%lang(pl) %{_mandir}/pl/man8/logoutd.8*
%lang(pl) %{_mandir}/pl/man8/userdel.8*
%lang(pl) %{_mandir}/pl/man8/usermod.8*
%lang(pl) %{_mandir}/pl/man8/vigr.8*
%lang(pl) %{_mandir}/pl/man8/vipw.8*

%lang(pt_BR) %{_mandir}/pt_BR/man1/gpasswd.1*
%lang(pt_BR) %{_mandir}/pt_BR/man5/passwd.5*
%lang(pt_BR) %{_mandir}/pt_BR/man5/shadow.5*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupadd.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupdel.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupmod.8*

%lang(ru) %{_mandir}/ru/man1/chage.1*
%lang(ru) %{_mandir}/ru/man1/chfn.1*
%lang(ru) %{_mandir}/ru/man1/chsh.1*
%lang(ru) %{_mandir}/ru/man1/expiry.1*
%lang(ru) %{_mandir}/ru/man1/gpasswd.1*
%lang(ru) %{_mandir}/ru/man1/groups.1*
%lang(ru) %{_mandir}/ru/man1/newgrp.1*
%lang(ru) %{_mandir}/ru/man1/passwd.1*
%lang(ru) %{_mandir}/ru/man1/sg.1*
%lang(ru) %{_mandir}/ru/man5/faillog.5*
%lang(ru) %{_mandir}/ru/man5/gshadow.5*
%lang(ru) %{_mandir}/ru/man5/login.defs.5*
%lang(ru) %{_mandir}/ru/man5/passwd.5*
%lang(ru) %{_mandir}/ru/man5/shadow.5*
%lang(ru) %{_mandir}/ru/man5/suauth.5*
%lang(ru) %{_mandir}/ru/man8/chgpasswd.8*
%lang(ru) %{_mandir}/ru/man8/chpasswd.8*
%lang(ru) %{_mandir}/ru/man8/faillog.8*
%lang(ru) %{_mandir}/ru/man8/groupadd.8*
%lang(ru) %{_mandir}/ru/man8/groupdel.8*
%lang(ru) %{_mandir}/ru/man8/groupmems.8*
%lang(ru) %{_mandir}/ru/man8/groupmod.8*
%lang(ru) %{_mandir}/ru/man8/grpck.8*
%lang(ru) %{_mandir}/ru/man8/grpconv.8*
%lang(ru) %{_mandir}/ru/man8/grpunconv.8*
%lang(ru) %{_mandir}/ru/man8/lastlog.8*
%lang(ru) %{_mandir}/ru/man8/logoutd.8*
%lang(ru) %{_mandir}/ru/man8/newusers.8*
%lang(ru) %{_mandir}/ru/man8/nologin.8*
%lang(ru) %{_mandir}/ru/man8/pwck.8*
%lang(ru) %{_mandir}/ru/man8/pwconv.8*
%lang(ru) %{_mandir}/ru/man8/pwunconv.8*
%lang(ru) %{_mandir}/ru/man8/useradd.8*
%lang(ru) %{_mandir}/ru/man8/userdel.8*
%lang(ru) %{_mandir}/ru/man8/usermod.8*
%lang(ru) %{_mandir}/ru/man8/vigr.8*
%lang(ru) %{_mandir}/ru/man8/vipw.8*

%lang(sv) %{_mandir}/sv/man1/chage.1*
%lang(sv) %{_mandir}/sv/man1/chsh.1*
%lang(sv) %{_mandir}/sv/man1/expiry.1*
%lang(sv) %{_mandir}/sv/man1/groups.1*
%lang(sv) %{_mandir}/sv/man1/newgrp.1*
%lang(sv) %{_mandir}/sv/man1/passwd.1*
%lang(sv) %{_mandir}/sv/man1/sg.1*
%lang(sv) %{_mandir}/sv/man5/faillog.5*
%lang(sv) %{_mandir}/sv/man5/gshadow.5*
%lang(sv) %{_mandir}/sv/man5/passwd.5*
%lang(sv) %{_mandir}/sv/man5/suauth.5*
%lang(sv) %{_mandir}/sv/man8/faillog.8*
%lang(sv) %{_mandir}/sv/man8/groupadd.8*
%lang(sv) %{_mandir}/sv/man8/groupdel.8*
%lang(sv) %{_mandir}/sv/man8/groupmems.8*
%lang(sv) %{_mandir}/sv/man8/groupmod.8*
%lang(sv) %{_mandir}/sv/man8/grpck.8*
%lang(sv) %{_mandir}/sv/man8/lastlog.8*
%lang(sv) %{_mandir}/sv/man8/logoutd.8*
%lang(sv) %{_mandir}/sv/man8/nologin.8*
%lang(sv) %{_mandir}/sv/man8/pwck.8*
%lang(sv) %{_mandir}/sv/man8/userdel.8*
%lang(sv) %{_mandir}/sv/man8/vigr.8*
%lang(sv) %{_mandir}/sv/man8/vipw.8*

%lang(tr) %{_mandir}/tr/man1/chage.1*
%lang(tr) %{_mandir}/tr/man1/chfn.1*
%lang(tr) %{_mandir}/tr/man1/passwd.1*
%lang(tr) %{_mandir}/tr/man5/passwd.5*
%lang(tr) %{_mandir}/tr/man5/shadow.5*
%lang(tr) %{_mandir}/tr/man8/groupadd.8*
%lang(tr) %{_mandir}/tr/man8/groupdel.8*
%lang(tr) %{_mandir}/tr/man8/groupmod.8*
%lang(tr) %{_mandir}/tr/man8/useradd.8*
%lang(tr) %{_mandir}/tr/man8/userdel.8*
%lang(tr) %{_mandir}/tr/man8/usermod.8*

%lang(zh_CN) %{_mandir}/zh_CN/man1/chage.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/chfn.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/chsh.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/expiry.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/gpasswd.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/groups.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/newgrp.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/passwd.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/sg.1*
%lang(zh_CN) %{_mandir}/zh_CN/man5/faillog.5*
%lang(zh_CN) %{_mandir}/zh_CN/man5/gshadow.5*
%lang(zh_CN) %{_mandir}/zh_CN/man5/login.defs.5*
%lang(zh_CN) %{_mandir}/zh_CN/man5/passwd.5*
%lang(zh_CN) %{_mandir}/zh_CN/man5/shadow.5*
%lang(zh_CN) %{_mandir}/zh_CN/man5/suauth.5*
%lang(zh_CN) %{_mandir}/zh_CN/man8/chgpasswd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/chpasswd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/faillog.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/groupadd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/groupdel.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/groupmems.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/groupmod.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/grpck.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/grpconv.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/grpunconv.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/lastlog.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/logoutd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/newusers.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/nologin.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/pwck.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/pwconv.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/pwunconv.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/useradd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/userdel.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/usermod.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/vigr.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/vipw.8*

%lang(zh_TW) %{_mandir}/zh_TW/man1/chfn.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/chsh.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/newgrp.1*
%lang(zh_TW) %{_mandir}/zh_TW/man5/passwd.5*
%lang(zh_TW) %{_mandir}/zh_TW/man8/chpasswd.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/groupadd.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/groupdel.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/groupmod.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/useradd.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/userdel.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/usermod.8*
