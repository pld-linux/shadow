Summary:	Shadow password file utilities for Linux
Summary(de):	Shadow-Paßwortdatei-Dienstprogramme für Linux
Summary(fr):	Fichiers utilitaires pour Shadow password pour Linux
Summary(pl):	Narzêdzia do obs³ugi shadow passwords
Summary(tr):	Gölge parola dosyasý araçlarý
Summary(pt_BR):	Utilitários para o arquivo de senhas Shadow
Summary(es):	Utilitarios para el archivo de contraseñas Shadow
Name:		shadow
Version:	4.0.0
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.pld.org.pl/software/shadow/%{name}-%{version}.tar.bz2
Source1:	%{name}-login.defs
Source2:	%{name}.useradd
Source3:	chage.pamd
Source4:	userdb.pamd
Source5:	chsh.pamd
Source6:	chfn.pamd
Source7:	passwd.pamd
Patch0:		%{name}-utmpx.patch
Patch1:		%{name}-pld.patch
BuildRequires:	pam-devel
Provides:	shadow-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	shadow-utils
Obsoletes:	passwd

%description
This package includes the programs necessary to convert standard UNIX
password files to the shadow password format, as well as programs for
command-line management of the user's accounts.
 - pwconv - converts everything to the shadow password format,
 - pwunconv - unconverts from shadow passwords, generating a file in
   the current directory called npasswd that is a standard UNIX password
   file,
 - pwck - checks the integrity of the password and shadow files,
 - lastlog - prints out the last login times of all users,
 - useradd, userdel, usermod - for accounts management,
 - groupadd, groupdel, groupmod - for group management.

A number of man pages are also included that relate to these
utilities, and shadow passwords in general.

%description -l pl
Pakiet zawiera programy do obs³ugi shadow password. Zanjduj± siê w nim
programy do konwersji standardowego pliku hase³ do wersji shadow
password a tak¿e programy do zarz±dania kontami u¿ytkowników w
systemie
 - pwconv - konwertuje do formatu shadow passwords
 - pwunconv - konwertuje z shadow passwords do formatu standardowego
   pliku hase³. W bie¿±cym katalogu tworzy plik npasswd bêd±cy
   standardowym plikiem z has³ami,
 - lastlog - wy¶wietla czas logowania u¿ytkowników,
 - useradd, userdel, usermod - do zarz±dzania kontami u¿ytkowników,
 - groupadd, groupdel, groupmod - do zarz±dzania grupami.

Ostrze¿enie:

Programy znajduj±ce siê w tym pakiecie s± niezbêdne do prawid³owej
pracy twojego systemu i podobnie jak pakiet z bibliotekami systemowymi
- glibc nigdy nie powinien zostaæ odinstalowany!

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

%package extras
Summary:	shadow - not often used files
Summary(pl):	shadow - pliki nie u¿ywane czêsto
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	%{name} = %{version}

%description extras
Programs for shadow often not used. If you have small system you may
skip them.

%description -l pl extras
Programy nie u¿ywane czêsto. W ma³ych systemach mo¿na je pomin±æ.

%prep
%setup -q 
%patch0 -p1 
%patch1 -p1 

%build
%configure \
	--disable-desrpc \
	--with-libcrypt \
	%{!?_without_static:--enable-static} \
	%{!?_without_static:--disable-shared} \
	%{?_without_static:--disable-static} \
	%{?_without_static:--enable-shared} \
	--with-libpam \
	--with-md5crypt \
	--with-nls \
	--without-included-gettext 
%{__make}  

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{default,pam.d,security,skel}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/login.defs
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/default/useradd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/chage
install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/shadow
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/chsh
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/chfn
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/passwd

:> $RPM_BUILD_ROOT%{_sysconfdir}/shadow
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/{chfn,chsh}.allow
touch $RPM_BUILD_ROOT%{_sysconfdir}/{porttime,utmp}

ln -sf vipw $RPM_BUILD_ROOT%{_sbindir}/vigr

echo .so newgrp.1 > $RPM_BUILD_ROOT%{_mandir}/man1/sg.1
echo .so vipw.8   > $RPM_BUILD_ROOT%{_mandir}/man8/vigr.8

echo .so newgrp.1 > $RPM_BUILD_ROOT%{_mandir}/pl/man1/sg.1
echo .so vipw.8   > $RPM_BUILD_ROOT%{_mandir}/pl/man8/vigr.8

echo .so newgrp.1 > $RPM_BUILD_ROOT%{_mandir}/ja/man1/sg.1

gzip -9nf doc/ANNOUNCE NEWS doc/README doc/README.linux doc/HOWTO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{!?_without_static:#}/sbin/ldconfig
if [ ! -f /etc/shadow ]; then
	%{_sbindir}/pwconv
fi

%{!?_without_static:#}%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.gz

%attr(750,root,root) %dir %{_sysconfdir}/default
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/default/*
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/chage
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/shadow
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/passwd
%attr(750,root,root) %dir /etc/security

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/login.defs
%attr(400,root,root) %ghost %{_sysconfdir}/shadow

%dir /etc/skel

%{!?_without_static:#}%attr(755,root,root) %{_libdir}/lib*
%attr(755,root,root) %{_sbindir}/user*
%attr(755,root,root) %{_sbindir}/group*
%attr(755,root,root) %{_sbindir}/grpck
%attr(755,root,root) %{_sbindir}/pwck
%attr(755,root,root) %{_sbindir}/*conv
%attr(755,root,root) %{_sbindir}/dpasswd
%attr(755,root,root) %{_sbindir}/vigr
%attr(755,root,root) %{_sbindir}/vipw
%attr(4755,root,root) %{_bindir}/passwd
%attr(755,root,root) %{_bindir}/faillog
%attr(755,root,root) %{_bindir}/groups
%attr(755,root,root) %{_bindir}/lastlog

#%{_mandir}/man1/login.*
%{_mandir}/man1/passwd.*
#%{_mandir}/man1/su.*
%{_mandir}/man5/faillog.*
#%{_mandir}/man5/limits.*	# it's not used when PAM is enabled?
%{_mandir}/man5/login.*
%{_mandir}/man5/passwd.*
%{_mandir}/man5/porttime.*
%{_mandir}/man5/shadow.*
%{_mandir}/man5/suauth.*
#%{_mandir}/man8/adduser.*	# no such program/symlink
%{_mandir}/man8/faillog.*
%{_mandir}/man8/groupadd.*
%{_mandir}/man8/groupdel.*
%{_mandir}/man8/groupmod.*
%{_mandir}/man8/grpck.*
%{_mandir}/man8/grpconv.*
%{_mandir}/man8/grpunconv.*
%{_mandir}/man8/lastlog.*
%{_mandir}/man8/pwck.*
%{_mandir}/man8/pwconv.*
%{_mandir}/man8/pwunconv.*
%{_mandir}/man8/useradd.*
%{_mandir}/man8/userdel.*
%{_mandir}/man8/usermod.*
%{_mandir}/man8/vigr.*
%{_mandir}/man8/vipw.*

%lang(pl) %{_mandir}/pl/man1/passwd.*
%lang(pl) %{_mandir}/pl/man5/faillog.*
%lang(pl) %{_mandir}/pl/man5/login.defs.*
%lang(pl) %{_mandir}/pl/man5/passwd.*
%lang(pl) %{_mandir}/pl/man5/shadow.*
%lang(pl) %{_mandir}/pl/man8/faillog.*
%lang(pl) %{_mandir}/pl/man8/groupadd.*
%lang(pl) %{_mandir}/pl/man8/groupdel.*
%lang(pl) %{_mandir}/pl/man8/groupmod.*
%lang(pl) %{_mandir}/pl/man8/grpck.*
%lang(pl) %{_mandir}/pl/man8/grpconv.*
%lang(pl) %{_mandir}/pl/man8/grpunconv.*
%lang(pl) %{_mandir}/pl/man8/lastlog.*
%lang(pl) %{_mandir}/pl/man8/pwck.*
%lang(pl) %{_mandir}/pl/man8/pwconv.*
%lang(pl) %{_mandir}/pl/man8/pwunconv.*
%lang(pl) %{_mandir}/pl/man8/useradd.*
%lang(pl) %{_mandir}/pl/man8/userdel.*
%lang(pl) %{_mandir}/pl/man8/usermod.*
%lang(pl) %{_mandir}/pl/man8/vigr.*
%lang(pl) %{_mandir}/pl/man8/vipw.*

%lang(ja) %{_mandir}/ja/man1/passwd.*
%lang(ja) %{_mandir}/ja/man5/faillog.*
%lang(ja) %{_mandir}/ja/man5/login.defs.*
%lang(ja) %{_mandir}/ja/man5/passwd.*
%lang(ja) %{_mandir}/ja/man5/shadow.*
%lang(ja) %{_mandir}/ja/man8/faillog.*
%lang(ja) %{_mandir}/ja/man8/groupadd.*
%lang(ja) %{_mandir}/ja/man8/groupdel.*
%lang(ja) %{_mandir}/ja/man8/groupmod.*
%lang(ja) %{_mandir}/ja/man8/grpck.*
%lang(ja) %{_mandir}/ja/man8/lastlog.*
%lang(ja) %{_mandir}/ja/man8/pwck.*
%lang(ja) %{_mandir}/ja/man8/pwconv.*
%lang(ja) %{_mandir}/ja/man8/userdel.*
%lang(ja) %{_mandir}/ja/man8/usermod.*

%lang(pt_BR) %{_mandir}/pt_BR/man5/shadow.*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupadd.*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupdel.*
%lang(pt_BR) %{_mandir}/pt_BR/man8/groupmod.*

%files extras
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/chsh
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/chfn
%attr(640,root,root) %config %verify(not size mtime md5) /etc/security/*
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/porttime
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/utmp
%attr(755,root,root) %{_bindir}/chage
%attr(4755,root,root) %{_bindir}/chfn
%attr(4755,root,root) %{_bindir}/chsh
%attr(4755,root,root) %{_bindir}/expiry
%attr(4755,root,root) %{_bindir}/gpasswd
%attr(4755,root,root) %{_bindir}/newgrp
%attr(755,root,root) %{_sbindir}/chpasswd
%attr(755,root,root) %{_sbindir}/mkpasswd
%attr(755,root,root) %{_sbindir}/newusers
%attr(755,root,root) %{_bindir}/sg
#%attr(755,root,root) %{_bindir}/su

%{_mandir}/man1/chage.*
%{_mandir}/man1/chfn.*
%{_mandir}/man1/chsh.*
%{_mandir}/man1/expiry.*
%{_mandir}/man1/gpasswd.*
%{_mandir}/man1/newgrp.*
%{_mandir}/man1/sg.*
%{_mandir}/man8/chpasswd.*
%{_mandir}/man8/mkpasswd.*
%{_mandir}/man8/newusers.*
%lang(pl) %{_mandir}/pl/man1/chage.*
%lang(pl) %{_mandir}/pl/man1/chfn.*
%lang(pl) %{_mandir}/pl/man1/chsh.*
%lang(pl) %{_mandir}/pl/man1/newgrp.*
%lang(pl) %{_mandir}/pl/man1/gpasswd.*
%lang(pl) %{_mandir}/pl/man1/sg.*
%lang(pl) %{_mandir}/pl/man8/chpasswd.*
%lang(pl) %{_mandir}/pl/man8/mkpasswd.*
%lang(pl) %{_mandir}/pl/man8/newusers.*

%lang(ja) %{_mandir}/ja/man1/chage.*
%lang(ja) %{_mandir}/ja/man1/chfn.*
%lang(ja) %{_mandir}/ja/man1/chsh.*
%lang(ja) %{_mandir}/ja/man1/gpasswd.*
%lang(ja) %{_mandir}/ja/man1/newgrp.*
%lang(ja) %{_mandir}/ja/man1/sg.*
%lang(ja) %{_mandir}/ja/man8/chpasswd.*
%lang(ja) %{_mandir}/ja/man8/mkpasswd.*

%lang(pt_BR) %{_mandir}/pt_BR/man1/gpasswd.*
