Summary:	Shadow password file utilities for Linux
Summary(de):	Shadow-Paßwortdatei-Dienstprogramme für Linux
Summary(fr):	Fichiers utilitaires pour Shadow password pour Linux.
Summary(pl):	Narzêdzia do obs³ugi shadow passwords
Summary(tr):	Gölge parola dosyasý araçlarý
Name:		shadow
Version:	19990307
Release:	2
Copyright:      BSD
Group:          Utilities/System
Group(pl):      Narzêdzia/System
URL:		ftp://ftp.ists.pwr.wroc.pl/pub/linux/shadow
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-login.defs
Source2:	%{name}.useradd
Patch0:		%{name}-%{version}-pld.patch
Patch1:		%{name}-utmpx.patch
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

%build
libtoolize --copy --force && aclocal && autoheader && automake && autoconf
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

make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    exec_prefix=$RPM_BUILD_ROOT \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    infodir$RPM_BUILD_ROOT=%{_infodir} \
    install

install -d $RPM_BUILD_ROOT/etc/default

install %{SOURCE1} $RPM_BUILD_ROOT/etc/login.defs
install %{SOURCE2} $RPM_BUILD_ROOT/etc/default/useradd

:> $RPM_BUILD_ROOT/etc/shadow

echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/pwunconv.8
echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/grpconv.8
echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/grpunconv.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[1358]/* \
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
%attr(755,root,root) %{_bindir}/chage
%attr(755,root,root) %{_bindir}/gpasswd
%attr(755,root,root) %{_bindir}/lastlog
%attr(755,root,root) %{_bindir}/faillog

%{_mandir}/man1/chage.1.gz
%{_mandir}/man1/gpasswd.1.gz
%{_mandir}/man3/shadow.3.gz
%{_mandir}/man5/shadow.5.gz
%{_mandir}/man5/faillog.5.gz
%{_mandir}/man8/group*.8.gz
%{_mandir}/man8/user*.8.gz
%{_mandir}/man8/pwck.8.gz
%{_mandir}/man8/grpck.8.gz
%{_mandir}/man8/chpasswd.8.gz 
%{_mandir}/man8/newusers.8.gz
%{_mandir}/man8/mkpasswd.8.gz
%{_mandir}/man8/*conv.8.gz
%{_mandir}/man8/lastlog.8.gz
%{_mandir}/man8/faillog.8.gz

%changelog
* Tue May 18 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [19990307-1]
- updated to latest version,
- removed old patches,
- %ghost /etc/shadow,
- FHS 2.0 && Unix98 changes,
- prepare for 1.0 PLD Linux ... 

* Tue Feb 02 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [981228-1d]
- updated to 981228,
- compressed documentation && man pages
- added Group(pl).

* Fri Oct 09 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [980724-1d]
- build against PLD Tornado,
- restricted files permissions,
- removed adduser,
- renamed invalid package name to shadow,
- added %postin scripts,
- fixed pl translation,
- minor changes.

* Tue Sep 1 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
- modify to build non-root,
- change mkdir to install -d,
- %attr makros,
- translations for pl,
- update source URL,
- start at RH  spec file.
