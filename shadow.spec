Summary:	Shadow password file utilities for Linux
Summary(de):	Shadow-Paßwortdatei-Dienstprogramme für Linux
Summary(fr):	Fichiers utilitaires pour Shadow password pour Linux.
Summary(pl):	Narzêdzia do obs³ugi shadow passwords
Summary(tr):	Gölge parola dosyasý araçlarý
Name:		shadow
Version:	19990827
Release:	1
Copyright:      BSD
Group:          Utilities/System
Group(pl):      Narzêdzia/System
Source0:	ftp://piast.t19.ds.pwr.wroc.pl/pub/linux/shadow/%{name}-%{version}.tar.gz
Source1:	%{name}-login.defs
Source2:	%{name}.useradd
Source3:	chage.pamd
Source4:	userdb.pamd
Patch0:		shadow-cvs.patch
Patch1:		shadow-pld.patch
Patch2:		shadow-utmpx.patch
Patch3:		shadow-pam-userdb.patch
Patch4:		shadow-DESTDIR.patch
BuildRequires:	pam-devel
BuildRequires:	gettext-devel
Requires:	pam
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package includes the programs necessary to convert standard
UNIX password files to the shadow password format, as well as 
programs for command-line management of the user's accounts.
        - 'pwconv' converts everything to the shadow password format.
        - 'pwunconv' unconverts from shadow passwords, generating a file 
           in the current directory called npasswd that is a standard UNIX 
           password file.
        - 'pwck' checks the integrity of the password and shadow files.
        - 'lastlog' prints out the last login times of all users.
	- 'useradd', 'userdel' and 'usermod' for accounts management.
	- 'groupadd', 'groupdel' and 'groupmod' for group management.

A number of man pages are also included that relate to these utilities,
and shadow passwords in general.

%description -l pl
Pakiet zawiera programy do obs³ugi shadow password. Zanjduj± siê w nim
programy do konwersji standardowego pliku hase³ do wersji shadow password
a tak¿e programy do zarz±danie kontami u¿ytkowników w systemie
	- 'pwconv' konwertuje do formatu shadow passwords
	- 'pwunconv' konwertuje z shadow passwords do formatu standardowego
	   pliku hase³. W bierz±cym katalogu tworzy plik npasswd bêd±cy
	   standardowym plikiem z has³ami.
	- 'lastlog' wy¶wietla czas logowanie u¿ytkowników
	-  'userdel' i 'usermod' do zarz±dzania kontami
	   u¿ytkowników.
	- 'groupadd', 'groupdel' and 'groupmod' do zarz±dzania grupami

Ostrze¿enie:

Programy znajduj±ce siê w tym pakiecie s± niezbêdne do prawid³owej pracy
twojego systemu i podobnie jak pakiet z bibliotekami systemowymi - glibc
nigdy nie powinien zostaæ odinstalowany !

%prep
%setup -q 
%patch0 -p1
%patch1 -p1 
%patch2 -p1 
%patch3 -p1
%patch4 -p1

%build
libtoolize --copy --force 
gettextize --copy --force
automake 
aclocal 
autoheader 
autoconf
%configure \
	--disable-desrpc \
	--with-libcrypt \
	--disable-shared \
	--with-libpam \
	--with-md5crypt \
	--with-nls \
	--without-included-gettext 
make  

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{default,pam.d}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/login.defs
install %{SOURCE2} $RPM_BUILD_ROOT/etc/default/useradd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/chage
install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/userdb

:> $RPM_BUILD_ROOT/etc/shadow

echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/pwunconv.8
echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/grpconv.8
echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/grpunconv.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	$RPM_BUILD_ROOT%{_mandir}/pl/man*/* \
	doc/ANNOUNCE doc/CHANGES doc/README doc/README.linux doc/HOWTO

%find_lang %{name}

%post
if [ ! -f /etc/shadow ]; then
%{_sbindir}/pwconv
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%doc doc/*.gz

%attr(750,root,root) %dir /etc/default
%attr(640,root,root) %config %verify(not size mtime md5) /etc/default/*
%attr(644,root,root) %config %verify(not size mtime md5) /etc/pam.d/*

%config(noreplace) %verify(not size mtime md5) /etc/login.defs
%attr(400,root,root) %ghost /etc/shadow

%attr(755,root,root) %{_sbindir}/user*
%attr(755,root,root) %{_sbindir}/group*
%attr(755,root,root) %{_sbindir}/grpck
%attr(755,root,root) %{_sbindir}/pwck
%attr(755,root,root) %{_sbindir}/*conv
%attr(755,root,root) %{_sbindir}/chpasswd
%attr(755,root,root) %{_sbindir}/newusers
%attr(755,root,root) %{_sbindir}/mkpasswd
%attr(755,root,root) %{_sbindir}/logoutd
%attr(755,root,root) %{_bindir}/chage
%attr(755,root,root) %{_bindir}/gpasswd
%attr(755,root,root) %{_bindir}/lastlog
%attr(755,root,root) %{_bindir}/faillog
%attr(755,root,root) %{_bindir}/sg
%attr(755,root,root) %{_bindir}/expiry

%{_mandir}/man1/gpasswd.*
%{_mandir}/man1/chage.*
%{_mandir}/man3/shadow.*
%{_mandir}/man5/login.defs.*
%{_mandir}/man5/passwd.*
%{_mandir}/man5/shadow.*
%{_mandir}/man5/porttime.*
%{_mandir}/man5/faillog.*
%{_mandir}/man8/dpasswd.*
%{_mandir}/man8/faillog.*
%{_mandir}/man8/groupdel.*
%{_mandir}/man8/groupmod.*
%{_mandir}/man8/grpck.*
%{_mandir}/man8/grpconv.*
%{_mandir}/man8/logoutd.*
%{_mandir}/man8/mkpasswd.*
%{_mandir}/man8/newusers.*
%{_mandir}/man8/pwck.*
%{_mandir}/man8/pwunconv.*
%{_mandir}/man8/useradd.*
%{_mandir}/man8/userdel.*
%{_mandir}/man8/usermod.*
%{_mandir}/man8/lastlog.*
%{_mandir}/man8/pwconv.*
%{_mandir}/man8/chpasswd.*
%{_mandir}/man8/groupadd.*
%{_mandir}/man8/grpunconv.*
%{_mandir}/man8/shadowconfig.*

%lang(pl) %{_mandir}/pl/man1/change.*
%lang(pl) %{_mandir}/pl/man1/gpasswd.*
%lang(pl) %{_mandir}/pl/man3/pw_auth.*
%lang(pl) %{_mandir}/pl/man5/faillog.*
%lang(pl) %{_mandir}/pl/man5/login.defs.*
%lang(pl) %{_mandir}/pl/man5/passwd.*
%lang(pl) %{_mandir}/pl/man5/porttime.*
%lang(pl) %{_mandir}/pl/man5/shadow.*
%lang(pl) %{_mandir}/pl/man8/chpasswd.*
%lang(pl) %{_mandir}/pl/man8/dpasswd.*
%lang(pl) %{_mandir}/pl/man8/faillog.*
%lang(pl) %{_mandir}/pl/man8/groupadd.*
%lang(pl) %{_mandir}/pl/man8/groupdel.*
%lang(pl) %{_mandir}/pl/man8/groupmod.*
%lang(pl) %{_mandir}/pl/man8/grpck.*
%lang(pl) %{_mandir}/pl/man8/lastlog.*
%lang(pl) %{_mandir}/pl/man8/logoutd.*
%lang(pl) %{_mandir}/pl/man8/mkpasswd.*
%lang(pl) %{_mandir}/pl/man8/newusers.*
%lang(pl) %{_mandir}/pl/man8/pwck.*
%lang(pl) %{_mandir}/pl/man8/pwconv.*
%lang(pl) %{_mandir}/pl/man8/pwuath.*
%lang(pl) %{_mandir}/pl/man8/shadowconfig.*
%lang(pl) %{_mandir}/pl/man8/useradd.*
%lang(pl) %{_mandir}/pl/man8/userdel.*
%lang(pl) %{_mandir}/pl/man8/usermod.*
