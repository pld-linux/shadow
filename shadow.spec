Summary:	Shadow password file utilities for Linux
Summary(de):	Shadow-Paßwortdatei-Dienstprogramme für Linux
Summary(fr):	Fichiers utilitaires pour Shadow password pour Linux.
Summary(pl):	Narzêdzia do obs³ugi shadow passwords
Summary(tr):	Gölge parola dosyasý araçlarý
Name:		shadow
Version:	981228
Release:	2
Copyright:      BSD
Group:          Utilities/System
Group(pl):      Narzêdzia/System
URL:		ftp://ftp.ists.pwr.wroc.pl/pub/linux/shadow
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-login.defs
Source2:	%{name}.useradd
Source3:	shells
Patch0:		shadow-man.patch
Patch1:		shadow-useradd.patch
Patch2:		shadow-groupadd.patch
Patch3:		shadow-getdef.patch
Buildroot:	/tmp/%{name}-%{version}-root
Obsoletes:	shadow-utils

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

%build
autoconf
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
    ./configure %{_target} \
	--prefix=/usr \
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

make install prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/default

install %{SOURCE1} $RPM_BUILD_ROOT/etc/login.defs
install %{SOURCE2} $RPM_BUILD_ROOT/etc/default/useradd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/shells

touch $RPM_BUILD_ROOT/etc/shadow

echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/pwunconv.8
echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/grpconv.8
echo .so pwconv.8 > $RPM_BUILD_ROOT%{_mandir}/man8/grpunconv.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[1358]/* \
	doc/ANNOUNCE doc/CHANGES doc/README doc/README.linux doc/HOWTO

%post
if [ ! -f /etc/shadow ]; then
/usr/sbin/pwconv
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc doc/*.gz

%attr(750,root,root) %dir /etc/default
%attr(640,root,root) %config %verify(not size mtime md5) /etc/default/*

%config(noreplace) %verify(not size mtime md5) /etc/login.defs
%config(noreplace) %verify(not size mtime md5) /etc/shells
%attr(400,root,root) %config(noreplace) %verify(not size mtime md5) /etc/shadow

%attr(755,root,root) /usr/sbin/user*
%attr(755,root,root) /usr/sbin/group*
%attr(755,root,root) /usr/sbin/grpck
%attr(755,root,root) /usr/sbin/pwck
%attr(755,root,root) /usr/sbin/*conv
%attr(755,root,root) /usr/sbin/chpasswd
%attr(755,root,root) /usr/sbin/newusers
%attr(755,root,root) /usr/sbin/mkpasswd
%attr(755,root,root) /usr/bin/chage
%attr(755,root,root) /usr/bin/gpasswd
%attr(755,root,root) /usr/bin/lastlog
%attr(755,root,root) /usr/bin/faillog

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

%lang(el) /usr/share/locale/el/LC_MESSAGES/shadow.mo

%changelog
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
- modify to build non-root
- change mkdir to install -d
- %attr makros
- translations for pl
- update source URL

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- Note that /usr/sbin/mkpasswd conflicts with /usr/bin/mkpasswd;
  one of these (I think /usr/sbin/mkpasswd but other opinions are valid)
  should probably be renamed.  In any case, mkpasswd.8 from this package
  needs to be installed. (problem #823)

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 980403
- redid the patches

* Tue Dec 30 1997 Cristian Gafton <gafton@redhat.com>
- updated the spec file
- updated the patch so that new accounts created on shadowed system won't
  confuse pam_pwdb anymore ('!!' default password instead on '!')
- fixed a bug that made useradd -G segfault
- the check for the ut_user is now patched into configure

* Thu Nov 13 1997 Erik Troan <ewt@redhat.com>
- added patch for XOPEN oddities in glibc headers
- check for ut_user before checking for ut_name -- this works around some
  confusion on glibc 2.1 due to the utmpx header not defining the ut_name
  compatibility stuff. I used a gross sed hack here because I couldn't make
  automake work properly on the sparc (this could be a glibc 2.0.99 problem
  though). The utuser patch works fine, but I don't apply it.
- sleep after running autoconf

* Thu Nov 06 1997 Cristian Gafton <gafton@redhat.com>
- added forgot lastlog command to the spec file

* Mon Oct 26 1997 Cristian Gafton <gafton@redhat.com>
- obsoletes adduser

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- modified groupadd; updated the patch

* Fri Sep 12 1997 Cristian Gafton <gafton@redhat.com>
- updated to 970616
- changed useradd to meet RH specs
- fixed some bugs

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
