# TODO
# - new files:
#   /etc/pam.d/chgpasswd
#   /etc/pam.d/chpasswd
#   /etc/pam.d/newusers
#   /usr/sbin/chgpasswd
#   /usr/sbin/nologin
#   /usr/share/man/man5/gshadow.5.gz
#   /usr/share/man/man8/chgpasswd.8.gz
#   /usr/share/man/man8/nologin.8.gz
# - check polish part in patch3
# - update shadow-po-update.patch
#
# Conditional build:
%bcond_without	selinux		# build without SE-Linux support
%bcond_with	shared		# build with shared libshadow
#
Summary:	Shadow password file utilities for Linux
Summary(de):	Shadow-Paßwortdatei-Dienstprogramme für Linux
Summary(es):	Utilitarios para el archivo de contraseñas Shadow
Summary(fr):	Fichiers utilitaires pour Shadow password pour Linux
Summary(pl):	Narzêdzia do obs³ugi mechanizmu ukrytych hase³
Summary(pt_BR):	Utilitários para o arquivo de senhas Shadow
Summary(tr):	Gölge parola dosyasý araçlarý
Name:		shadow
Version:	4.0.16
Release:	0.8
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.pld.org.pl/software/shadow/%{name}-%{version}.tar.bz2
# Source0-md5:	1d91f7479143d1d705b94180c0d4874b
Source1:	%{name}-login.defs
Source2:	%{name}.useradd
Source3:	chage.pamd
Source4:	userdb.pamd
Source5:	chsh.pamd
Source6:	chfn.pamd
Source7:	passwd.pamd
Source8:	useradd.pamd
Patch0:		%{name}-pld.patch
Patch1:		%{name}-chage_expdays.patch
Patch2:		%{name}-po-update.patch
Patch3:		%{name}-typo.patch
BuildRequires:	autoconf
BuildRequires:	automake >= 1.0
BuildRequires:	gettext-devel >= 0.12.1
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool
BuildRequires:	pam-devel
Requires:	pam >= 0.77.3
# to force proper coreutils version, so "groups" command exists
Requires:	/usr/bin/groups
Provides:	passwd
Provides:	shadow-utils
Obsoletes:	passwd
Obsoletes:	shadow-utils
Conflicts:	pwdutils
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

%description -l es
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

%description -l pl
Pakiet zawiera programy do obs³ugi mechanizmu ukrytych hase³ (shadow
password). Znajduj± siê w nim programy do konwersji standardowego
pliku hase³ do wersji shadow password a tak¿e programy do zarz±dzania
kontami u¿ytkowników w systemie:
- pwconv - konwertuje do formatu shadow password
- pwunconv - konwertuje z shadow password do formatu standardowego
  pliku hase³. W bie¿±cym katalogu tworzy plik npasswd bêd±cy
  standardowym plikiem z has³ami,
- lastlog - wy¶wietla czas logowania u¿ytkowników,
- useradd, userdel, usermod - do zarz±dzania kontami u¿ytkowników,
- groupadd, groupdel, groupmod - do zarz±dzania grupami.

Ostrze¿enie:

Programy znajduj±ce siê w tym pakiecie s± niezbêdne do prawid³owej
pracy systemu i podobnie jak pakiet z bibliotekami systemowymi (glibc)
nigdy nie powinien zostaæ odinstalowany!

%description -l pt_BR
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

%package extras
Summary:	shadow - not often used programs
Summary(pl):	shadow - programy nieczêsto u¿ywane
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	pwdutils
Conflicts:	util-linux < 2.12-10

%description extras
Programs for shadow not often used. If you have small system you may
skip them.

%description extras -l pl
Programy nieczêsto u¿ywane. W ma³ych systemach mo¿na je pomin±æ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

# ugh, too populated to patch
%{__sed} -i -e 's/instead DES/instead of DES/' src/chpasswd.c po/*.po

rm -f po/stamp-po

%build
%{__autoheader}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-desrpc \
	%{?with_shared:--enable-shared --disable-static} \
	--without-libcrack \
	--with-libcrypt \
	--with-libpam \
	--with-md5crypt \
	--with-nls \
	%{?with_selinux:--with-selinux} \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{default,pam.d,security,skel/tmp}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/login.defs
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/default/useradd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/chage
install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/shadow
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/chsh
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/chfn
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/passwd
install %{SOURCE8} $RPM_BUILD_ROOT/etc/pam.d/useradd
sed -e 's/usermod/userdel/' etc/pam.d/usermod > $RPM_BUILD_ROOT/etc/pam.d/userdel
install etc/pam.d/usermod $RPM_BUILD_ROOT/etc/pam.d/usermod
install etc/pam.d/groupadd $RPM_BUILD_ROOT/etc/pam.d/groupadd
install etc/pam.d/groupmod $RPM_BUILD_ROOT/etc/pam.d/groupmod
install etc/pam.d/groupdel $RPM_BUILD_ROOT/etc/pam.d/groupdel

> $RPM_BUILD_ROOT%{_sysconfdir}/shadow
> $RPM_BUILD_ROOT/etc/security/chfn.allow
> $RPM_BUILD_ROOT/etc/security/chsh.allow

# vigr symlink is created by make install, but in wrong dir
ln -sf vipw $RPM_BUILD_ROOT%{_sbindir}/vigr

# what's this for?
echo '.so newgrp.1' > $RPM_BUILD_ROOT%{_mandir}/it/man1/sg.1

%if %{without shared}
# invalid static library
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

# no -devel, be gone
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# included in glibc-devel
rm -f $RPM_BUILD_ROOT%{_mandir}{,*/}/man3/{getspnam,shadow}.3
# /bin/login already in login (from util-linux.spec)
rm -f $RPM_BUILD_ROOT{%{_bindir}/login,/etc/pam.d/login,%{_sbindir}/logoutd,%{_mandir}/{,*/}man1/login.1,%{_mandir}/{,*/}man5/porttime.5,%{_mandir}/{,*/}man8/logoutd.8}
# /bin/id already in coreutils
rm -f $RPM_BUILD_ROOT%{_mandir}{,*/}/man1/id.1
# /bin/su already in coreutils
rm -f $RPM_BUILD_ROOT{%{_bindir}/su,/etc/pam.d/su,%{_mandir}/{,*/}man1/su.1}
# /usr/bin/groups already in coreutils
rm -f $RPM_BUILD_ROOT{%{_bindir}/groups,%{_mandir}/{,*/}man1/groups.1}
# /etc/limits not used with pam
rm -f $RPM_BUILD_ROOT%{_mandir}/{,*/}man5/limits.5

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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/passwd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/shadow
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/useradd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/usermod
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/userdel
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/groupadd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/groupdel
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/groupmod
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/login.defs
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/shadow
%dir /etc/skel
%dir /etc/skel/tmp
%{?with_shared:%attr(755,root,root) %{_libdir}/lib*.so.*.*}
%attr(755,root,root) %{_sbindir}/chpasswd
%attr(755,root,root) %{_sbindir}/groupadd
%attr(755,root,root) %{_sbindir}/groupdel
%attr(755,root,root) %{_sbindir}/groupmod
%attr(755,root,root) %{_sbindir}/grpck
%attr(755,root,root) %{_sbindir}/grpconv
%attr(755,root,root) %{_sbindir}/grpunconv
%attr(755,root,root) %{_sbindir}/pwck
%attr(755,root,root) %{_sbindir}/pwconv
%attr(755,root,root) %{_sbindir}/pwunconv
%attr(755,root,root) %{_sbindir}/useradd
%attr(755,root,root) %{_sbindir}/userdel
%attr(755,root,root) %{_sbindir}/usermod
%attr(755,root,root) %{_sbindir}/vigr
%attr(755,root,root) %{_sbindir}/vipw
%attr(755,root,root) %{_bindir}/faillog
%attr(755,root,root) %{_bindir}/lastlog
%attr(4755,root,root) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*
%{_mandir}/man5/faillog.5*
%{_mandir}/man5/login.defs.5*
%{_mandir}/man5/passwd.5*
%{_mandir}/man5/shadow.5*
%{_mandir}/man5/suauth.5*
%{_mandir}/man8/faillog.8*
%{_mandir}/man8/groupadd.8*
%{_mandir}/man8/groupdel.8*
%{_mandir}/man8/groupmod.8*
%{_mandir}/man8/grpck.8*
%{_mandir}/man8/grpconv.8*
%{_mandir}/man8/grpunconv.8*
%{_mandir}/man8/lastlog.8*
%{_mandir}/man8/pwck.8*
%{_mandir}/man8/pwconv.8*
%{_mandir}/man8/pwunconv.8*
%{_mandir}/man8/useradd.8*
%{_mandir}/man8/userdel.8*
%{_mandir}/man8/usermod.8*
%{_mandir}/man8/vigr.8*
%{_mandir}/man8/vipw.8*
%{_mandir}/man8/chpasswd.8*

%lang(cs) %{_mandir}/cs/man5/passwd.5*
%lang(cs) %{_mandir}/cs/man5/shadow.5*
%lang(cs) %{_mandir}/cs/man5/faillog.5*
%lang(cs) %{_mandir}/cs/man8/faillog.8*
%lang(cs) %{_mandir}/cs/man8/groupadd.8*
%lang(cs) %{_mandir}/cs/man8/groupdel.8*
%lang(cs) %{_mandir}/cs/man8/groupmod.8*
%lang(cs) %{_mandir}/cs/man8/grpck.8*
%lang(cs) %{_mandir}/cs/man8/lastlog.8*
%lang(cs) %{_mandir}/cs/man8/vipw.8*

%lang(de) %{_mandir}/de/man1/passwd.1*
%lang(de) %{_mandir}/de/man8/vigr.8*
%lang(de) %{_mandir}/de/man8/vipw.8*
%lang(de) %{_mandir}/de/man5/passwd.5*

%lang(es) %{_mandir}/es/man1/passwd.1*
%lang(es) %{_mandir}/es/man5/passwd.5*
%lang(es) %{_mandir}/es/man8/vigr.8*
%lang(es) %{_mandir}/es/man8/vipw.8*

%lang(fi) %{_mandir}/fi/man1/passwd.1*

%lang(fr) %{_mandir}/fr/man1/passwd.1*
%lang(fr) %{_mandir}/fr/man5/faillog.5*
%lang(fr) %{_mandir}/fr/man5/login.defs.5*
%lang(fr) %{_mandir}/fr/man5/passwd.5*
%lang(fr) %{_mandir}/fr/man5/shadow.5*
%lang(fr) %{_mandir}/fr/man5/suauth.5*
%lang(fr) %{_mandir}/fr/man8/chpasswd.8*
%lang(fr) %{_mandir}/fr/man8/faillog.8*
%lang(fr) %{_mandir}/fr/man8/groupadd.8*
%lang(fr) %{_mandir}/fr/man8/groupdel.8*
%lang(fr) %{_mandir}/fr/man8/groupmod.8*
%lang(fr) %{_mandir}/fr/man8/grpck.8*
%lang(fr) %{_mandir}/fr/man8/grpconv.8*
%lang(fr) %{_mandir}/fr/man8/grpunconv.8*
%lang(fr) %{_mandir}/fr/man8/lastlog.8*
%lang(fr) %{_mandir}/fr/man8/pwck.8*
%lang(fr) %{_mandir}/fr/man8/pwconv.8*
%lang(fr) %{_mandir}/fr/man8/pwunconv.8*
%lang(fr) %{_mandir}/fr/man8/useradd.8*
%lang(fr) %{_mandir}/fr/man8/userdel.8*
%lang(fr) %{_mandir}/fr/man8/usermod.8*
%lang(fr) %{_mandir}/fr/man8/vigr.8*
%lang(fr) %{_mandir}/fr/man8/vipw.8*

%lang(hu) %{_mandir}/hu/man1/passwd.1*

%lang(id) %{_mandir}/id/man8/useradd.8*

%lang(it) %{_mandir}/it/man1/passwd.1*
%lang(it) %{_mandir}/it/man5/passwd.5*
%lang(it) %{_mandir}/it/man5/shadow.5*
%lang(it) %{_mandir}/it/man8/groupadd.8*
%lang(it) %{_mandir}/it/man8/groupdel.8*
%lang(it) %{_mandir}/it/man8/groupmod.8*
%lang(it) %{_mandir}/it/man8/grpck.8*
%lang(it) %{_mandir}/it/man8/grpconv.8*
%lang(it) %{_mandir}/it/man8/grpunconv.8*
%lang(it) %{_mandir}/it/man8/lastlog.8*
%lang(it) %{_mandir}/it/man8/pwconv.8*
%lang(it) %{_mandir}/it/man8/pwunconv.8*
%lang(it) %{_mandir}/it/man8/useradd.8*
%lang(it) %{_mandir}/it/man8/userdel.8*
%lang(it) %{_mandir}/it/man8/usermod.8*
%lang(it) %{_mandir}/it/man8/vigr.8*
%lang(it) %{_mandir}/it/man8/vipw.8*

%lang(ja) %{_mandir}/ja/man1/passwd.1*
%lang(ja) %{_mandir}/ja/man5/faillog.5*
%lang(ja) %{_mandir}/ja/man5/login.defs.5*
%lang(ja) %{_mandir}/ja/man5/passwd.5*
%lang(ja) %{_mandir}/ja/man5/shadow.5*
%lang(ja) %{_mandir}/ja/man5/suauth.5*
%lang(ja) %{_mandir}/ja/man8/faillog.8*
%lang(ja) %{_mandir}/ja/man8/groupadd.8*
%lang(ja) %{_mandir}/ja/man8/groupdel.8*
%lang(ja) %{_mandir}/ja/man8/groupmod.8*
%lang(ja) %{_mandir}/ja/man8/grpck.8*
%lang(ja) %{_mandir}/ja/man8/grpconv.8*
%lang(ja) %{_mandir}/ja/man8/grpunconv.8*
%lang(ja) %{_mandir}/ja/man8/lastlog.8*
%lang(ja) %{_mandir}/ja/man8/pwck.8*
%lang(ja) %{_mandir}/ja/man8/pwconv.8*
%lang(ja) %{_mandir}/ja/man8/pwunconv.8*
%lang(ja) %{_mandir}/ja/man8/useradd.8*
%lang(ja) %{_mandir}/ja/man8/userdel.8*
%lang(ja) %{_mandir}/ja/man8/usermod.8*
%lang(ja) %{_mandir}/ja/man8/vigr.8*
%lang(ja) %{_mandir}/ja/man8/vipw.8*

%lang(ko) %{_mandir}/ko/man5/passwd.5*
%lang(ko) %{_mandir}/ko/man8/vigr.8*
%lang(ko) %{_mandir}/ko/man8/vipw.8*

%lang(pl) %{_mandir}/pl/man1/passwd.1*
%lang(pl) %{_mandir}/pl/man5/faillog.5*
%lang(pl) %{_mandir}/pl/man5/login.defs.5*
%lang(pl) %{_mandir}/pl/man5/passwd.5*
%lang(pl) %{_mandir}/pl/man5/shadow.5*
%lang(pl) %{_mandir}/pl/man5/suauth.5*
%lang(pl) %{_mandir}/pl/man8/faillog.8*
%lang(pl) %{_mandir}/pl/man8/groupadd.8*
%lang(pl) %{_mandir}/pl/man8/groupdel.8*
%lang(pl) %{_mandir}/pl/man8/groupmod.8*
%lang(pl) %{_mandir}/pl/man8/grpck.8*
%lang(pl) %{_mandir}/pl/man8/grpconv.8*
%lang(pl) %{_mandir}/pl/man8/grpunconv.8*
%lang(pl) %{_mandir}/pl/man8/lastlog.8*
%lang(pl) %{_mandir}/pl/man8/pwck.8*
%lang(pl) %{_mandir}/pl/man8/pwconv.8*
%lang(pl) %{_mandir}/pl/man8/pwunconv.8*
%lang(pl) %{_mandir}/pl/man8/useradd.8*
%lang(pl) %{_mandir}/pl/man8/userdel.8*
%lang(pl) %{_mandir}/pl/man8/usermod.8*
%lang(pl) %{_mandir}/pl/man8/vigr.8*
%lang(pl) %{_mandir}/pl/man8/vipw.8*

# FIXME change to -> pt?
%lang(pt_BR) %{_mandir}/pt_BR/man5/passwd.5*
%lang(pt_BR) %{_mandir}/pt_BR/man5/shadow.5*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupadd.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupdel.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupmod.8*

%lang(ru) %{_mandir}/ru/man1/passwd.1*
%lang(ru) %{_mandir}/ru/man5/faillog.5*
%lang(ru) %{_mandir}/ru/man5/login.defs.5*
%lang(ru) %{_mandir}/ru/man5/passwd.5*
%lang(ru) %{_mandir}/ru/man5/shadow.5*
%lang(ru) %{_mandir}/ru/man5/suauth.5*
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
%lang(ru) %{_mandir}/ru/man8/pwck.8*
%lang(ru) %{_mandir}/ru/man8/pwconv.8*
%lang(ru) %{_mandir}/ru/man8/pwunconv.8*
%lang(ru) %{_mandir}/ru/man8/useradd.8*
%lang(ru) %{_mandir}/ru/man8/userdel.8*
%lang(ru) %{_mandir}/ru/man8/usermod.8*
%lang(ru) %{_mandir}/ru/man8/vigr.8*
%lang(ru) %{_mandir}/ru/man8/vipw.8*

%lang(tr) %{_mandir}/tr/man1/passwd.1*
%lang(tr) %{_mandir}/tr/man5/passwd.5*
%lang(tr) %{_mandir}/tr/man5/shadow.5*
%lang(tr) %{_mandir}/tr/man8/groupadd.8*
%lang(tr) %{_mandir}/tr/man8/groupdel.8*
%lang(tr) %{_mandir}/tr/man8/groupmod.8*
%lang(tr) %{_mandir}/tr/man8/useradd.8*
%lang(tr) %{_mandir}/tr/man8/userdel.8*
%lang(tr) %{_mandir}/tr/man8/usermod.8*

%lang(zh_CN) %{_mandir}/zh_CN/man8/chpasswd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/groupadd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/groupdel.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/groupmod.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/useradd.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/userdel.8*
%lang(zh_CN) %{_mandir}/zh_CN/man8/usermod.8*

%lang(zh_TW) %{_mandir}/zh_TW/man8/groupadd.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/groupdel.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/groupmod.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/useradd.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/userdel.8*
%lang(zh_TW) %{_mandir}/zh_TW/man8/usermod.8*

%files extras
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chfn
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chsh
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/chfn.allow
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/chsh.allow
%attr(755,root,root) %{_bindir}/chage
%attr(4755,root,root) %{_bindir}/chfn
%attr(4755,root,root) %{_bindir}/chsh
%attr(4755,root,root) %{_bindir}/expiry
%attr(4755,root,root) %{_bindir}/gpasswd
%attr(755,root,root) %{_bindir}/newgrp
%attr(755,root,root) %{_bindir}/sg
%attr(755,root,root) %{_sbindir}/newusers

%{_mandir}/man1/chage.1*
%{_mandir}/man1/chfn.1*
%{_mandir}/man1/chsh.1*
%{_mandir}/man1/expiry.1*
%{_mandir}/man1/gpasswd.1*
%{_mandir}/man1/newgrp.1*
%{_mandir}/man1/sg.1*
%{_mandir}/man8/newusers.8*

%lang(cs) %{_mandir}/cs/man1/expiry.1*
%lang(cs) %{_mandir}/cs/man1/gpasswd.1*

%lang(de) %{_mandir}/de/man1/chfn.1*
%lang(de) %{_mandir}/de/man1/chsh.1*
%lang(de) %{_mandir}/de/man1/newgrp.1*

%lang(es) %{_mandir}/es/man1/newgrp.1*

%lang(fi) %{_mandir}/fi/man1/chfn.1*
%lang(fi) %{_mandir}/fi/man1/chsh.1*

%lang(fr) %{_mandir}/fr/man1/chage.1*
%lang(fr) %{_mandir}/fr/man1/chfn.1*
%lang(fr) %{_mandir}/fr/man1/chsh.1*
%lang(fr) %{_mandir}/fr/man1/expiry.1*
%lang(fr) %{_mandir}/fr/man1/gpasswd.1*
%lang(fr) %{_mandir}/fr/man1/newgrp.1*
%lang(fr) %{_mandir}/fr/man1/sg.1*
%lang(fr) %{_mandir}/fr/man8/newusers.8*

%lang(hu) %{_mandir}/hu/man1/chsh.1*
%lang(hu) %{_mandir}/hu/man1/gpasswd.1*
%lang(hu) %{_mandir}/hu/man1/newgrp.1*
%lang(hu) %{_mandir}/hu/man1/sg.1*
%lang(hu) %{_mandir}/hu/man5/passwd.5*
%lang(hu) %{_mandir}/hu/man8/lastlog.8*

%lang(id) %{_mandir}/id/man1/chsh.1*

%lang(it) %{_mandir}/it/man1/chage.1*
%lang(it) %{_mandir}/it/man1/chfn.1*
%lang(it) %{_mandir}/it/man1/chsh.1*
%lang(it) %{_mandir}/it/man1/expiry.1*
%lang(it) %{_mandir}/it/man1/gpasswd.1*
%lang(it) %{_mandir}/it/man1/newgrp.1*
%lang(it) %{_mandir}/it/man1/sg.1*
%lang(it) %{_mandir}/it/man5/faillog.5*
%lang(it) %{_mandir}/it/man8/chpasswd.8*
%lang(it) %{_mandir}/it/man8/faillog.8*
%lang(it) %{_mandir}/it/man8/newusers.8*
%lang(it) %{_mandir}/it/man8/pwck.8*

%lang(ja) %{_mandir}/ja/man1/chage.1*
%lang(ja) %{_mandir}/ja/man1/chfn.1*
%lang(ja) %{_mandir}/ja/man1/chsh.1*
%lang(ja) %{_mandir}/ja/man1/expiry.1*
%lang(ja) %{_mandir}/ja/man1/gpasswd.1*
%lang(ja) %{_mandir}/ja/man1/newgrp.1*
%lang(ja) %{_mandir}/ja/man1/sg.1*
%lang(ja) %{_mandir}/ja/man8/chpasswd.8*
%lang(ja) %{_mandir}/ja/man8/newusers.8*

%lang(ko) %{_mandir}/ko/man1/chfn.1*
%lang(ko) %{_mandir}/ko/man1/chsh.1*
# missing in tarball
#%lang(ko) %{_mandir}/ko/man1/newgrp.1*

%lang(ru) %{_mandir}/ru/man1/chage.1*
%lang(ru) %{_mandir}/ru/man1/chfn.1*
%lang(ru) %{_mandir}/ru/man1/chsh.1*
%lang(ru) %{_mandir}/ru/man1/expiry.1*
%lang(ru) %{_mandir}/ru/man1/gpasswd.1*
%lang(ru) %{_mandir}/ru/man1/newgrp.1*
%lang(ru) %{_mandir}/ru/man1/sg.1*
%lang(ru) %{_mandir}/ru/man8/newusers.8*

%lang(pl) %{_mandir}/pl/man1/chage.1*
%lang(pl) %{_mandir}/pl/man1/chfn.1*
%lang(pl) %{_mandir}/pl/man1/chsh.1*
%lang(pl) %{_mandir}/pl/man1/expiry.1*
%lang(pl) %{_mandir}/pl/man1/gpasswd.1*
%lang(pl) %{_mandir}/pl/man1/newgrp.1*
%lang(pl) %{_mandir}/pl/man1/sg.1*
%lang(pl) %{_mandir}/pl/man8/chpasswd.8*
%lang(pl) %{_mandir}/pl/man8/newusers.8*

%lang(pt_BR) %{_mandir}/pt_BR/man1/gpasswd.1*

%lang(tr) %{_mandir}/tr/man1/chage.1*
%lang(tr) %{_mandir}/tr/man1/chfn.1*

%lang(zh_CN) %{_mandir}/zh_CN/man1/chfn.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/chsh.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/newgrp.1*
%lang(zh_CN) %{_mandir}/zh_CN/man5/passwd.5*

%lang(zh_TW) %{_mandir}/zh_TW/man1/chfn.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/chsh.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/newgrp.1*
%lang(zh_TW) %{_mandir}/zh_TW/man5/passwd.5*
%lang(zh_TW) %{_mandir}/zh_TW/man8/chpasswd.8*
